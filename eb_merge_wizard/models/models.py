# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger('base.task.merge.automatic.wizard')
class MergeTasksLine(models.TransientModel):

    _name = 'base.task.merge.line'
    _order = 'min_id asc'

    wizard_id = fields.Many2one('base.task.merge.automatic.wizard', 'Wizard')
    min_id = fields.Integer('MinID')
    aggr_ids = fields.Char('Ids', required=True)

class EbMergeTasks(models.TransientModel):

    _name = 'base.task.merge.automatic.wizard'
    _description = 'Merge Tasks'

    @api.model
    def default_get(self, fields):
        res = super(EbMergeTasks, self).default_get(fields)
        active_ids = self.env.context.get('active_ids')
        if self.env.context.get('active_model') == 'project.task' and active_ids:
            res['task_ids'] = active_ids
        return res

    task_ids = fields.Many2many('project.task', string='Tasks')#'merge_tasks_rel', 'merge_id', 'task_id',)
    user_id = fields.Many2one('res.users', 'Assigned to', index=True)
    dst_task_id = fields.Many2one('project.task', string='Destination Task')
    dst_project = fields.Many2one('project.project', string = "Project")


    @api.multi
    def action_merge(self):
        names=[]
        #write the name of the destination task because it will overwritten
        if self.dst_task_id:
            names.append(self.dst_task_id.name)
        else:
            raise UserError(_("You must select a Destination Task"))


        desc=[]
        #also write the description of the destination task because it will be overwritten
        desc.append(self.dst_task_id.description)
        for id in self.task_ids:
            if id.id != self.dst_task_id.id:
                for name in id:
                    names.append(name.name)
                    desc.append(name.description)
                #self.task_ids.write({'message_ids' : self.dst_task_id.message_ids})
        #transfering the messages from task_ids to dst_task_id
        for message in self.task_ids:
            for msg_id in message.message_ids:
                msg_id.write({'res_id': self.dst_task_id.id})

        #Transfer the timesheets from task_ids to dst_task_id
        
        for timesheet in self.task_ids:
            for ts_id in timesheet.timesheet_ids:
                ts_id.write({'task_id': self.dst_task_id.id})
                    #the task id for timesheet is updated with the dst_task_id.id

        # # #loop the task_ids and transfer the tag_ids to the dst_task_id
        for task in self.task_ids:
            for tag in task.tag_ids:
                tag.write({'tag_ids': (6, 0, [self.dst_task_id.id])})



        #Check for planned hours and if any collect them all and place dst_task_id
        plan_hours = self.dst_task_id.planned_hours
        for hour in self.task_ids:
            for time in hour:
                plan_hours+=time.planned_hours
        #Write to dst_task_id full planned hours from all tasks
        self.dst_task_id.write({'planned_hours': plan_hours})

        #actual writing to the tasks
        transformed_names = ', '.join([unicode(i) for i in names])
        self.dst_task_id.write({'name' : transformed_names})

        # mapping with lambda prints with BRACKETS []  ---> map(lambda x: x.encode('ascii'), names)

        transformed_desc = ', '.join([unicode(i) for i in desc])
        self.dst_task_id.write({'description' : transformed_desc})

        # mapping with lambda prints with BRACKETS []  ---> map(lambda x: x.encode('ascii'), desc)
        #Posting a note in the merged and archived tasks
        ###################################################################
        #get the base url from ir.config_parameter
        base_url   =  self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        #loop all active tasks
        for task in self.task_ids:
            #post the link to every task
            task.message_post(body="This task has been merged into: " '%s/#id=%s&amp;view_type=form&amp;model=project.task' % (base_url, self.dst_task_id.id))

        self.task_ids.write({'active':False})
        #explicitly write the dst_task_id TRUE for ACTIVE for security reasons

        self.dst_task_id.write({'active':True})

        #Check if user has been assigned and if not raise error

        if self.user_id.id:
        #write the Assiged TO user_id
            self.dst_task_id.write({'user_id' : self.user_id.id})
        elif self.dst_task_id.user_id.id:
                self.dst_task_id.write({'user_id' : self.dst_task_id.user_id.id})
        else:
            raise UserError(_("There is no user assigned to the merged task, and the destination task doesn't have assigned user too!!!"))


        #For project_id check if any is given from user, if not use the project_id from dst_task_id project
        #write the project id to the dst_task_id
        if self.dst_project:
            self.dst_task_id.write({'project_id': self.dst_project.id})
        else:
            self.dst_task_id.write({'project_id': self.dst_task_id.project_id.id})

        return True

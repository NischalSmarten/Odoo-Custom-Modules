from odoo import models, fields, api


class ProductTemplate(models.Model):

    _inherit ="product.template"

    image_url = fields.Char("Image Url",compute="_compute_image_url")

    def _compute_image_url(self):

        for rec in self:
            rec.image_url= f"{rec.get_base_url()}/web/image/product.template/{rec.id}/image_1920"
            
    


class ProductProduct(models.Model):
    _inherit = "product.product"
    
    variant_url = fields.Char("Variant Url",compute="_compute_variant_url")
    
    def _compute_variant_url(self):
        
        for rec in self:
            rec.variant_url= f"{rec.get_base_url()}/web/image?model=product.product&id={rec.id}&field=image_128"
            
            
            
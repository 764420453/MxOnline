import xadmin
from apps.users.models import EmailVerifyRecord, Banner
from xadmin import views



class BaseSetting(object):
    enable_themes = True  # 开启主题功能
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"
xadmin.site.register(views.CommAdminView, GlobalSettings)




class EmailVerifyRecordAdmin(object):
    list_display=['code','email','send_type','send_time']
    search_fields=['code','email','send_type']
    list_filter=['code','email','send_type','send_time']

class BannerAdmin(object):
    list_display=['title','image','url','index','add_time']
    search_fields=['title','image','url','index']
    list_filter=['title','image','url','index','add_time']
xadmin.site.register(Banner,BannerAdmin)





xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
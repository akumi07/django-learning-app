from django.contrib import admin
from .models import chaiVariety, chaiReview, Store, chaiCertificate

class ChaiReviewInline(admin.TabularInline):
    model = chaiReview
    extra = 1

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    filter_horizontal = ('chai_Variety',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issue_date')

admin.site.register(chaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(chaiCertificate, ChaiCertificateAdmin)
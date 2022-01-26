from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views 
from  django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('',views.index,name='index.html'),
    path('admin/', admin.site.urls),
    path('',views.about_us,name='about_us.html'),
    path('',views.add_streaming,name='add_streaming.html'),
    path('',views.all_instructor,name='all_instructor.html'),
    path('',views.apply_job,name='apply_job.html'),
    path('',views.base,name='base.html'),
    path('',views.blog_single_view,name='blog_single_view.html'),
    path('',views.career,name='career.html'),
    path('',views.certification_center,name='certification_center.html'),
    path('',views.thank_you,name='thank_you.html'),
    path('',views.terms_of_use,name='terms_of_use.html'),
    path('',views.sitemap,name='sitemap.html'),
    path('',views.sign_up,name='sign_up.html'),
    path('',views.sign_up_steps,name='sign_up_steps.html'),
    path('',views.sign_in,name='sign_in.html'),
    path('',views.shopping_cart,name='shopping_cart.html'),
    path('',views.setting,name='setting.html'),
    path('',views.search_result,name='search_result.html'),
    path('',views.saved_courses,name='saved_courses.html'),
    path('',views.report_history,name='report_history.html'),
    path('',views.press,name='press.html'),
    path('',views.our_blog,name='our_blog.html'),
    path('',views.my_instructor_profile_view,name='my_instructor_profile_view.html'),
    path('',views.membership,name='index.html'),
    path('',views.login,name='login.html'),
    path('',views.live_streams,name='live_streams.html'),
    path('',views.live_output,name='live_output.html'),
    path('',views.invoice,name='invoice.html'),
    path('',views.instructor_verification,name='instructor_verification.html'),
    path('',views.instructor_statements,name='instructor_statements.html'),
    path('',views.instructor_profile_view,name='instructor_profile_view.html'),
    path('',views.instructor_payout,name='instructor_payout.html'),
    path('',views.instructor_notifications,name='instructor_notifications.html'),
    path('',views.instructor_my_certificates,name='instructor_my_certificates.html'),
    path('',views.instructor_messages,name='instructor_messages.html'),
    path('',views.instructor_earning,name='instructor_earning.html'),
    path('',views.instructor_dashboard,name='instructor_dashboard.html'),
    path('',views.instructor_courses,name='instructor_courses.html'),
    path('',views.instructor_analyics,name='instructor_analyics.html'),
    path('',views.instructor_all_reviews,name='instructor_all_reviews.html'),
    path('',views.forgot_password,name='forgot_password.html'),
    path('',views.help,name='help.html'),
    path('',views.feedback,name='feedback.html'),
    path('',views.explore,name='explore.html'),
    path('',views.error_404,name='error_404.html'),
    path('',views.create_new_course,name='create_new_course.html'),
    path('',views.course_detail_view,name='course_detail_view.html'),
    path('',views.contact_us,name='contact_us.html'),
    path('',views.company_details,name='company_details.html'),
    path('',views.coming_soon,name='coming_soon.html'),
    path('',views.checkout_membership,name='checkout_membership.html'),
    path('',views.certification_test_view,name='certification_test_view.html'),
    path('',views.certification_test_result,name='certification_test_result.html'),
    path('',views.certification_start_form,name='certification_start_form.html'),
    path('accounts/', include('accounts.urls'))

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

from django.conf import settings

# ... your normal urlpatterns here

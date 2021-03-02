from django.views.generic import ListView, DetailView, TemplateView
from django.apps import apps

class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # context['app_list'] = ['playermanagement', 'survey']

        dictVerbose= {}
        # apps.get_app_configs() 메소드는 settings.py 파일의 INSTALLED_APPS에 등록된
        # 각 앱의 클래스들을 담은 리스트를 반환
        for app in apps.get_app_configs():
            # 애플리케이션의 경로에 site-packages가 들어 있으면 외부 라이브러리 애플리케이션임
            # 현재 프로젝트의 앱만
            if 'site-packages' not in app.path:
                # dictVerbose= {app.label : app.verbose_name }
                dictVerbose[app.label] = app.verbose_name
        context['verbose_dict'] = dictVerbose
        return context









"""
Django settings for web_project1 project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

with open(os.path.join(BASE_DIR,'web_set', 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['192.168.0.10', 'localhost', '127.0.0.1']

LOGGING = {
    # 고정값; 현재는 버전이 하나뿐임
    'version': 1,
    # 기존의 로거들을 비활성화하지 않음 -> 활성화함
    # 디폴트는 True임
    'disable_existing_loggers': False,

    # 포맷터 1개 정의; 로그를 출력할 형식을 정의
    'formatters': {
        'verbose': {
            # 포맷터 : [로그메시지 기록시간], 로그 레벨 이름, [로그이름:라인번호], 로그메시지
            # asctime 시간
            # name 로거이름
            # levelname 로깅레벨
            # message 메세지
            # 출처: https://hamait.tistory.com/880 [HAMA 블로그]
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            # 데이트 포맷 : 날짜/월축약형/연도 시(24시 기준):분:초
            'datefmt' : "%d/%b/%Y %H:%M:%S"
                },
            },

    'handlers': {
        # file 핸들러 정의
        # DEBUG 이상의 메시지를 파일로 출력함
        # BASE_DIR : D:\WEB_study\My_web_study2\python_web\python_web_project1

        # verbose 포맷터 사용
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs','web_project1.log'),
            'formatter' : 'verbose',
        },
    },

    'loggers': {
        # 디폴트로 설정된 django 로거를 오버라이딩함
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        # 로거의 이름을 survey로 함; 나중에 __name__ 변수로 로거를 취득하기 위해
        # DEBUG 이상의 메시지를 file 핸들러에 보냄(로그 메시지 파일에 기록)
        'survey': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

# Application definition

INSTALLED_APPS = [
    'survey.apps.SurveyConfig', # 추가함
    'playermanagement.apps.PlayerManagementConfig', # 추가함
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.account.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web_project1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'web_project1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db',  'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'web_set', 'static')










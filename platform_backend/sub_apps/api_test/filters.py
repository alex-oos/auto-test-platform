#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:filters.py
@time:2021/11/27
@email:tao.xu2008@outlook.com
@description: 过滤器
"""

import django_filters
from django_filters.rest_framework import FilterSet
from apps.api_test.models import Project, ProjectMember, ApiGroup, ApiInfo, ApiUpdateHistory, YApiEvent, \
    TestSuite, TestCase, TestStep, TestReport


class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class ProjectFilter(FilterSet):
    department__isnull = django_filters.CharFilter(field_name='department__id', lookup_expr='isnull')

    class Meta:
        model = Project
        fields = {
            'name': ['icontains'],
            'department': ['exact']
        }


class ProjectMemberFilter(FilterSet):
    user__username = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')

    class Meta:
        model = ProjectMember
        fields = {
            'project': ['exact'],
            'status': ['exact'],
            'role': ['exact'],
        }


class ApiGroupFilter(FilterSet):
    class Meta:
        model = ApiGroup
        fields = {
            'name': ['icontains'],
            'project': ['exact']
        }


class ApiInfoFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    project__id__in = NumberInFilter(field_name='project__id', lookup_expr='in')
    update_status__gt = django_filters.BooleanFilter(field_name='update_status', lookup_expr='gt')
    step_api__id__isnull = django_filters.BooleanFilter(field_name='step_api__id', lookup_expr='isnull')
    create_time__gte = django_filters.DateFilter(field_name='create_time', lookup_expr='gte')
    create_time__lte = django_filters.DateFilter(field_name='create_time', lookup_expr='lte')

    class Meta:
        model = ApiInfo
        fields = {
            'name': ['icontains'],
            'project': ['exact'],
            'api_group': ['exact'],
            'api_group_id': ['exact'],
            'update_status': ['exact'],
        }


class ApiUpdateHistoryFilter(FilterSet):
    api__id__in = NumberInFilter(field_name='api__id', lookup_expr='in')
    update_status__in = NumberInFilter(field_name='update_status', lookup_expr='in')
    update_status__gt = django_filters.BooleanFilter(field_name='update_status', lookup_expr='gt')

    class Meta:
        model = ApiUpdateHistory
        fields = {
            'id': ['icontains'],
            'api__id': ['exact'],
            'update_status': ['exact']
        }


class YApiEventFilter(FilterSet):
    class Meta:
        model = YApiEvent
        fields = {
            'id': ['icontains'],
            'event': ['exact']
        }


class TestSuiteFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    id_in = NumberInFilter(field_name='id', lookup_expr='in')
    department__in = NumberInFilter(field_name='department__id', lookup_expr='in')
    department__isnull = django_filters.CharFilter(field_name='department__id', lookup_expr='isnull')
    labels__in = django_filters.BaseInFilter(field_name='labels', lookup_expr='in')

    class Meta:
        model = TestSuite
        fields = {
            'id': ['exact'],
            'name': ['icontains'],
            'department': ['exact']
        }


class TestCaseFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    result__in = django_filters.BaseInFilter(field_name='result', lookup_expr='in')
    id_in = NumberInFilter(field_name='id', lookup_expr='in')
    test_suite__in = NumberInFilter(field_name='test_suite', lookup_expr='in')
    create_time__gte = django_filters.DateFilter(field_name='create_time', lookup_expr='gte')
    create_time__lte = django_filters.DateFilter(field_name='create_time', lookup_expr='lte')

    class Meta:
        model = TestCase
        fields = {
            'id': ['exact'],
            'name': ['icontains'],
            'test_suite': ['exact']
        }


class TestStepFilter(FilterSet):
    result__in = django_filters.BaseInFilter(field_name='result', lookup_expr='in')
    id_in = NumberInFilter(field_name='id', lookup_expr='in')
    test_case__in = NumberInFilter(field_name='test_case', lookup_expr='in')
    apiInfo__in = NumberInFilter(field_name='apiInfo', lookup_expr='in')
    apiInfo__project__in = NumberInFilter(field_name='apiInfo__project', lookup_expr='in')
    create_time__gte = django_filters.DateFilter(field_name='create_time', lookup_expr='gte')
    create_time__lte = django_filters.DateFilter(field_name='create_time', lookup_expr='lte')

    class Meta:
        model = TestStep
        fields = {
            'id': ['exact'],
            'description': ['icontains'],
            'test_case': ['exact'],
            'apiInfo__id': ['exact'],
            'apiInfo__project__id': ['exact']
        }


class TestReportFilter(FilterSet):
    id_in = NumberInFilter(field_name='id', lookup_expr='in')
    create_time__after = django_filters.DateTimeFilter(field_name='create_time', lookup_expr='gte')
    create_time__before = django_filters.DateTimeFilter(field_name='create_time', lookup_expr='lte')

    class Meta:
        model = TestReport
        fields = {
            'id': ['exact'],
            'status': ['exact'],
        }


if __name__ == '__main__':
    pass

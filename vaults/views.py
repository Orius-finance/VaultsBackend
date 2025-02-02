from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action


class VaultsDetail(viewsets.ViewSet):
    def get(self, request):
        pass

    @action("tvl", detail=True)
    def get_tvl(self, request):
        pass

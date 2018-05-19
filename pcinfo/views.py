import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import dateutil.parser as dparser
import os.path, time

from pcinfo.models import PC, MOTHERBOARD, RAM, GPU, OS, HDD, CPU


class MainPage(TemplateView):
    pass


class PcinfoTable(TemplateView):
    def get_context_data(self, *args, **kwargs):
        """
            Если мы получили GET запрос.
        """
        context = super(PcinfoTable, self).get_context_data(**kwargs)
        path = 'D:\\pcinfo'
        # path = 'templates\\pcinfo'
        # f = open('C:\\Users\\admin\\PycharmProjects\\web_map\\templates\\pcinfo\\10.1.52.11.txt')
        files = []
        for d, dirs, fs in os.walk(path):
            if d == path:
                files = fs
        i = 0
        PCs = []
        for file in files:
            try:
                if file.split(".")[len(file.split(".")) - 1] == "txt":
                    i += 1
                    PC = []
                    name = file
                    filechanged = time.ctime(os.path.getmtime(path + "\\" + str(file)))
                    f = open(path + "\\" + str(file))
                    file = []
                    for line in f:
                        file.append(line)
                    # print(str(i) + ". " + f.name + "    |   " + file[2][file[2].rfind(':') + 1:len(file[2]) - 1])
                    try:
                        PC.append(i)
                        PC.append(file[0][file[0].rfind(':') + 1:len(file[0]) - 1])
                        PC.append(file[2][file[2].rfind(':') + 1:len(file[2]) - 1])
                        PC.append(file[3][file[3].rfind(':') + 1:len(file[3]) - 1])
                        PC.append(file[4][file[4].rfind(':') + 1:len(file[4]) - 1])
                        PC.append(dparser.parse(file[5][file[5].rfind(':') + 1:len(file[5]) - 1]))
                        PC.append(int(file[14][file[14].rfind(':') + 1:len(file[14]) - 1]))
                        PC.append(file[11][file[11].rfind(':') + 1:len(file[11]) - 1])
                        PC.append(dparser.parse(filechanged))
                        PC.append(name)
                    except Exception as e:
                        print(e)
                    PCs.append(PC)
                    f.close()
                    # PC['IP'] =
            except Exception as e:
                pass
        PCsOut = []
        for i in range(len(PCs)):
            finder = False
            for j in range(len(PCs)):
                if PCs[i][2] == PCs[j][2] and PCs[j][9] != PCs[i][9]:
                    if PCs[i][8] > PCs[j][8]:
                        finder = True
            if not finder:
                PCsOut.append(PCs[i])

        if "sort_id" in context:
            n = int(context['sort_id'])
        else:
            n = 0

        def sort_col(i):
            return i[n]

        PCsOut.sort(key=sort_col)
        context['PCs'] = PCsOut
        context['selected'] = [5, 11, 14, 15, 20, 21, 27]
        context['page'] = 1
        return context


class TableGenerator(TemplateView):
    def get_context_data(self, *args, **kwargs):
        """
            Если мы получили GET запрос.
        """
        context = super(PcinfoTable, self).get_context_data(**kwargs)
        path = '\\\\b1-fileshare\\pcinfo'
        # path = 'templates\\pcinfo'
        # f = open('C:\\Users\\admin\\PycharmProjects\\web_map\\templates\\pcinfo\\10.1.52.11.txt')
        files = []
        for d, dirs, fs in os.walk(path):
            files = fs
        i = 0

        PCs = []
        for file in files:
            try:
                if file.split(".")[len(file.split(".")) - 1] == "txt":
                    i += 1
                    PC = []
                    name = file
                    filechanged = time.ctime(os.path.getmtime(path + "\\" + str(file)))
                    f = open(path + "\\" + str(file))
                    file = []
                    for line in f:
                        file.append(line)
                    # print(str(i) + ". " + f.name + "    |   " + file[2][file[2].rfind(':') + 1:len(file[2]) - 1])
                    try:
                        PC.append(i)
                        PC.append(file[0][file[0].rfind(':') + 1:len(file[0]) - 1])
                        PC.append(file[2][file[2].rfind(':') + 1:len(file[2]) - 1])
                        PC.append(file[3][file[3].rfind(':') + 1:len(file[3]) - 1])
                        PC.append(file[4][file[4].rfind(':') + 1:len(file[4]) - 1])
                        PC.append(dparser.parse(file[5][file[5].rfind(':') + 1:len(file[5]) - 1]))
                        PC.append(int(file[14][file[14].rfind(':') + 1:len(file[14]) - 1]))
                        PC.append(file[11][file[11].rfind(':') + 1:len(file[11]) - 1])
                        PC.append(dparser.parse(filechanged))
                        PC.append(name)
                    except Exception as e:
                        print(e)
                    PCs.append(PC)
                    f.close()
                    # PC['IP'] =
            except Exception as e:
                pass
        PCsOut = []
        for i in range(len(PCs)):
            finder = False
            for j in range(len(PCs)):
                if PCs[i][2] == PCs[j][2] and PCs[j][9] != PCs[i][9]:
                    if PCs[i][8] > PCs[j][8]:
                        finder = True
            if not finder:
                PCsOut.append(PCs[i])

        if "sort_id" in context:
            n = int(context['sort_id'])
        else:
            n = 0

        def sort_col(i):
            return i[n]

        PCsOut.sort(key=sort_col)
        context['PCs'] = PCsOut
        context['selected'] = [5, 11, 14, 15, 20, 21, 27]
        context['page'] = 1
        return context


class Support(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Support).get_context_data(**kwargs)
        return context


class DataGetter(TemplateView):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('cp866'))
        print(data)
        pc = PC.objects.create(
            ip=data['ip'],
            bios_manufacturer=data['bios']['manifacturer'],
            bios_version=data['bios']['version'],
        )
        for item in data['motherboard']:
            pc.motherboard.add(MOTHERBOARD.objects.create(
                name=data['motherboard'][item]['name'],
                manufacturer=data['motherboard'][item]['manufacturer'],
                chipset=data['motherboard'][item]['chipset'],
                serial_number=data['motherboard'][item]['serial_number'],
            ))
        for item in data['ram']:
            pc.ram.add(RAM.objects.create(
                name=data['ram'][item]['name'],
                manufacturer=data['ram'][item]['manufacturer'],
                capacity=data['ram'][item]['capacity'],
                form_factor=data['ram'][item]['form_factor'],
                clock_speed=data['ram'][item]['clock_speed'],
            ))
        for item in data['gpu']:
            pc.gpu.add(GPU.objects.create(
                name=data['gpu'][item]['name'],
                manufacturer=data['gpu'][item]['manufacturer'],
                adapter_ram=data['gpu'][item]['adapter_ram'],
                driver_version=data['gpu'][item]['driver_version'],
                video_processor=data['gpu'][item]['video_processor'],
            ))
        for item in data['os']:
            pc.os.add(OS.objects.create(
                name=data['os'][item]['name'],
                manufacturer=data['os'][item]['manufacturer'],
                caption=data['os'][item]['caption'],
                version=data['os'][item]['version'],
                computer_name=data['os'][item]['computer_name'],
                current_user=data['os'][item]['current_user'],
                install_date=data['os'][item]['install_date'],
                build_number=data['os'][item]['build_number'],
                boot_device=data['os'][item]['boot_device'],
                total_visible_memory=data['os'][item]['total_visible_memory'],
                serial_number=data['os'][item]['serial_number'],
            ))
        for item in data['hdd']:
            pc.hdd.add(HDD.objects.create(
                name=data['hdd'][item]['name'],
            ))
        for item in data['cpu']:
            pc.cpu.add(CPU.objects.create(
                name=data['cpu'][item]['name'],
                manufacturer=data['cpu'][item]['manufacturer'],
                core_count=data['cpu'][item]['core_count'],
                clock_speed=data['cpu'][item]['clock_speed'],
                architecture=data['cpu'][item]['architecture'],
            ))
        pc.save()
        return HttpResponse('OK')

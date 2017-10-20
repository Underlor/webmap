import os
from django.shortcuts import render
from django.views.generic import TemplateView
import dateutil.parser as dparser


class MainPage(TemplateView):
    pass


class PcinfoTable(TemplateView):
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
            if file.split(".")[len(file.split(".")) - 1] == "txt":
                i += 1
                PC = []
                f = open(path + "\\" + str(file))
                file = []
                for line in f:
                    file.append(line)
                print(str(i) + ". " + f.name + "    |   " + file[2][file[2].rfind(':') + 1:len(file[2]) - 1])
                try:
                    PC.append(i)
                    PC.append(file[0][file[0].rfind(':') + 1:len(file[0]) - 1])
                    PC.append(file[2][file[2].rfind(':') + 1:len(file[2]) - 1])
                    PC.append(file[3][file[3].rfind(':') + 1:len(file[3]) - 1])
                    PC.append(file[4][file[4].rfind(':') + 1:len(file[4]) - 1])
                    PC.append(dparser.parse(file[5][file[5].rfind(':') + 1:len(file[5]) - 1]))
                    PC.append(int(file[14][file[14].rfind(':') + 1:len(file[14]) - 1]))
                    PC.append(file[11][file[11].rfind(':') + 1:len(file[11]) - 1])
                except Exception as e:
                    print(e)
                PCs.append(PC)
                f.close()
                # PC['IP'] =
        if "sort_id" in context:
            n = int(context['sort_id'])
        else:
            n = 0

        def sort_col(i):
            return i[n]

        PCs.sort(key=sort_col)
        context['PCs'] = PCs
        context['selected'] = [5, 11, 14, 15, 19, 20, 21, 27]
        context['page'] = 0
        return context

# Create your views here.

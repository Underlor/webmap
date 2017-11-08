import datetime
from redminelib import Redmine

redmine = Redmine('https://redmine.inntech.studio', username='a.popov@inntech.studio', password='MuzveovCaf')
project = redmine.project.get('inntech-studio')


def create_task():
    issue = redmine.issue.create(
        project_id=1,
        subject='Test API',  # Тема
        tracker_id=4,
        # Трэкер (6 - Другое, 3 - Поддержка, 4 - Обращения пользователей, 7 - Неисправность, 2 - Улучшение)
        description='ПОМАГИТЕ!!!!',  # Описание
        status_id=1,  # Статус
        priority_id=2,  # Приоритет (1 - Низкий, 2 - Нормальный, 3 - Высокий, 4 - Срочный, 5 - Немедленный)
        assigned_to_id=6,  # Назначена (6 - Дмитрий Куценко, 17 - Александр Попов)
        watcher_user_ids=[],
        start_date=datetime.datetime.now().date(),
        estimated_hours=4,
        done_ratio=0,
        uploads=[]
    )

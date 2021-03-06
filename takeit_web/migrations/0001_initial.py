# Generated by Django 2.2.4 on 2019-10-14 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('phone', models.CharField(db_index=True, help_text='전화번호 (id로 쓰임)', max_length=255, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True, help_text='회원 탈퇴 플래그')),
                ('nickname', models.CharField(max_length=16, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('status', models.CharField(choices=[('FAILURE_PAYMENT', '결제 실패'), ('WAITING_PAYMENT', '결제 대기중'), ('NEW', '새 주문'), ('REJECTED', '주문 거절'), ('IN_PROGRESS', '제조 중'), ('MANUFACTURED', '제조 완료'), ('DELIVERED', '전달 완료')], default='WAITING_PAYMENT', help_text='진행 상황', max_length=32)),
                ('grand_total', models.IntegerField(help_text='총 합계(결제 금액)')),
                ('name', models.CharField(help_text='커피 외 n건', max_length=31)),
                ('orderer_request', models.CharField(blank=True, help_text='고객님 요청사항', max_length=500)),
                ('orderer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('name', models.CharField(help_text='가게 이름', max_length=64)),
                ('street_address', models.CharField(help_text='도로명 주소(신 주소)', max_length=128)),
                ('place', models.CharField(help_text='숭실대학교 학생회관 4층', max_length=64)),
                ('owner_phone', models.CharField(help_text='점주 전화번호', max_length=20)),
                ('note', models.TextField(blank=True, help_text='비고 등 기타 메모')),
                ('is_opened', models.BooleanField(default=False)),
                ('using_point_system', models.BooleanField(default=True)),
                ('store_detail', models.TextField(blank=True, default=list, help_text="가게 영업 시간, 휴무 등의 상세정보, [{'key': 'value'}] 형태")),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='store', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('priority', models.PositiveIntegerField(default=0, help_text='앱에 표시될 때의 우선순위')),
                ('description', models.CharField(blank=True, max_length=128)),
                ('default_price', models.IntegerField(default=3000)),
                ('options', models.TextField(blank=True, default=list, help_text='이용 가능한 옵션')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='takeit_web.Store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('options', models.TextField(help_text='이용 가능한 옵션')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='takeit_web.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takeit_web.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='takeit_web.Store'),
        ),
    ]

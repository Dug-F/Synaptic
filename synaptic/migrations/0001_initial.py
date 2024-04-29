# Generated by Django 5.0.4 on 2024-04-29 19:21

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import synaptic.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CheckStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20, verbose_name='Check Status')),
            ],
            options={
                'verbose_name_plural': 'Check Statuses',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='RoomMemberStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20, verbose_name='Room Member Status')),
            ],
            options={
                'verbose_name_plural': 'RoomMemberStatuses',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='RoomStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20, verbose_name='Room Status')),
            ],
            options={
                'verbose_name_plural': 'Room Statuses',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='TransitionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20, verbose_name='Transition Type')),
                ('function', models.CharField(max_length=20, null=True, verbose_name='Function')),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='UserExtension',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.PositiveIntegerField(verbose_name='Question Number')),
                ('question', models.CharField(blank=True, max_length=255, verbose_name='Question')),
                ('media_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Media Url')),
                ('default_image_number', models.PositiveIntegerField(null=True, verbose_name='Default Image')),
                ('time_limit', models.PositiveIntegerField(default=30, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)], verbose_name='Time Limit (secs)')),
                ('score_multiplier', models.DecimalField(decimal_places=2, default=1, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='Score Multiplier')),
                ('answer_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Answer 1')),
                ('correct_answer_1', models.BooleanField(verbose_name='Correct Answer')),
                ('answer_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Answer 2')),
                ('correct_answer_2', models.BooleanField(verbose_name='Correct Answer')),
                ('answer_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Answer 3')),
                ('correct_answer_3', models.BooleanField(verbose_name='Correct Answer')),
                ('answer_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Answer 4')),
                ('correct_answer_4', models.BooleanField(verbose_name='Correct Answer')),
                ('status', models.ForeignKey(default=synaptic.models.get_default_check_status_pk, on_delete=django.db.models.deletion.CASCADE, to='synaptic.checkstatus', verbose_name='Question Status')),
            ],
            options={
                'ordering': ['question_number'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_number', models.PositiveIntegerField(verbose_name='Answer Number')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
                ('correct_answer', models.BooleanField(verbose_name='Correct Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers_in_question', to='synaptic.question', verbose_name='Question')),
            ],
            options={
                'ordering': ['answer_number'],
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('quiz_date', models.DateField(default=datetime.date.today, verbose_name='Quiz Date')),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(blank=True, default=synaptic.models.get_default_check_status_pk, on_delete=django.db.models.deletion.CASCADE, to='synaptic.checkstatus', verbose_name='Quiz Status')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
                'ordering': ['created_date', 'title'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_in_quiz', to='synaptic.quiz', verbose_name='Quiz'),
        ),
        migrations.CreateModel(
            name='QuizRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.PositiveIntegerField(verbose_name='Room Number')),
                ('question_start_time', models.DateTimeField(blank=True, null=True, verbose_name='Question Start Time')),
                ('countdown_seconds_remaining', models.PositiveIntegerField(verbose_name='Countdown Remaining')),
                ('opened_date', models.DateField(default=datetime.date.today, verbose_name='Opened Date')),
                ('preview', models.BooleanField(default=False)),
                ('current_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synaptic.question', verbose_name='Current Question')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('last_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_questions_in_quizzes', to='synaptic.question', verbose_name='Last Question')),
                ('previous_question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='previous_questions_in_quizzes', to='synaptic.question', verbose_name='Previous Question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synaptic.quiz', verbose_name='Quiz')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synaptic.roomstatus', verbose_name='Room Status')),
            ],
        ),
        migrations.CreateModel(
            name='QuizRoomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30, verbose_name='Nickname')),
                ('joined_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('preview', models.BooleanField(default=False)),
                ('joker_status', models.BooleanField(default=False, verbose_name='Joker Status')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_in_quiz', to='synaptic.quizroom', verbose_name='Room Number')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_in_room', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_in_room_status', to='synaptic.roommemberstatus', verbose_name='Room Member Status')),
            ],
            options={
                'ordering': ['room', 'user'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='transition_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='synaptic.transitiontype', verbose_name='Transition Type'),
        ),
        migrations.CreateModel(
            name='QuizRoomMemberAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.PositiveIntegerField(verbose_name='Question Number')),
                ('answer_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Answer Number')),
                ('response_time', models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True, verbose_name='Response Time')),
                ('answer_score', models.PositiveIntegerField(blank=True, null=True, verbose_name='Running Score')),
                ('running_score', models.PositiveIntegerField(blank=True, null=True, verbose_name='Prior Running Score')),
                ('running_score_prior', models.PositiveIntegerField(blank=True, null=True, verbose_name='Answer Score')),
                ('joker_status', models.BooleanField(default=False, verbose_name='Joker Status')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers_in_room_member', to='synaptic.answer', verbose_name='Answer')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions_in_room_member', to='synaptic.question', verbose_name='Question')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_in_room', to='synaptic.quizroom', verbose_name='Room')),
                ('room_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_in_room_member', to='synaptic.quizroommember', verbose_name='Room Member')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_from_member', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['room', 'user', 'question', 'answer'],
                'indexes': [models.Index(fields=['room'], name='synaptic_qu_room_id_0bc06d_idx'), models.Index(fields=['user'], name='synaptic_qu_user_id_0ed656_idx'), models.Index(fields=['room', 'user'], name='synaptic_qu_room_id_24ecaa_idx'), models.Index(fields=['room', 'question'], name='synaptic_qu_room_id_f2d019_idx')],
                'unique_together': {('room', 'user', 'question', 'answer')},
            },
        ),
        migrations.AddIndex(
            model_name='quizroommember',
            index=models.Index(fields=['room'], name='synaptic_qu_room_id_7eb665_idx'),
        ),
        migrations.AddIndex(
            model_name='quizroommember',
            index=models.Index(fields=['user'], name='synaptic_qu_user_id_95fafc_idx'),
        ),
        migrations.AddIndex(
            model_name='quizroommember',
            index=models.Index(fields=['room', 'user'], name='synaptic_qu_room_id_75d071_idx'),
        ),
        migrations.AddIndex(
            model_name='quizroommember',
            index=models.Index(fields=['room', 'user', 'status'], name='synaptic_qu_room_id_ce7b05_idx'),
        ),
        migrations.AddIndex(
            model_name='quizroommember',
            index=models.Index(fields=['room', 'user', 'nickname'], name='synaptic_qu_room_id_215250_idx'),
        ),
    ]

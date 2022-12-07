from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gadjets(models.Model):
    id = models.TextField(primary_key=True)
    folder = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    gadjets = models.TextField(blank=True, null=True)
    mac = models.TextField(blank=True, null=True)
    device_type = models.TextField(blank=True, null=True)
    last_event = models.TextField(blank=True, null=True)
    functions = models.TextField(blank=True, null=True)
    device_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gadjets'


class Gusers(models.Model):
    userid = models.AutoField(primary_key=True)
    password = models.TextField()
    email = models.TextField(blank=True, null=True)
    phone_numper = models.TextField(blank=True, null=True)
    pcon_count = models.IntegerField()
    username = models.TextField(blank=True, null=True)
    pass_field = models.TextField(db_column='pass', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'gusers'


class Indata(models.Model):
    taskid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    pconid = models.IntegerField()
    voltage = models.FloatField(blank=True, null=True)
    amperage = models.FloatField(blank=True, null=True)
    systematwork = models.BooleanField(blank=True, null=True)
    systemerror = models.IntegerField(blank=True, null=True)
    switchinfo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indata'


class IndataEvent(models.Model):
    taskid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    pconid = models.IntegerField()
    voltage = models.FloatField(blank=True, null=True)
    amperage = models.FloatField(blank=True, null=True)
    systematwork = models.BooleanField(blank=True, null=True)
    systemerror = models.IntegerField(blank=True, null=True)
    switchinfo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indata_event'


class Notifications(models.Model):
    folder = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    error_icon = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class Outdata(models.Model):
    taskid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    pconid = models.IntegerField()
    switchposition = models.BooleanField(blank=True, null=True)
    systemask = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outdata'


class OutdataEvent(models.Model):
    taskid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    pconid = models.IntegerField()
    switchposition = models.BooleanField(blank=True, null=True)
    systemask = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outdata_event'

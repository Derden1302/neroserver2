from django.db import models


class Actions(models.Model):
    id = models.UUIDField(primary_key=True)
    type = models.CharField(max_length=40, blank=True, null=True)
    title = models.CharField(max_length=40, blank=True, null=True)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'actions'


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


class Gadgets(models.Model):
    id = models.UUIDField(primary_key=True)
    status = models.BooleanField(blank=True, null=True)
    folder = models.UUIDField(blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    mac = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'gadgets'


class Gusers(models.Model):
    userid = models.UUIDField(primary_key=True)
    password = models.CharField(max_length=30)
    phone_numper = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gusers'


class Indata(models.Model):
    taskid = models.BigIntegerField(primary_key=True)
    id = models.ForeignKey(Gadgets, models.DO_NOTHING, db_column='id')
    voltage = models.FloatField()
    amperage = models.FloatField()
    times = models.TextField(db_column='timeS')  # Field name made lowercase. This field type is a guess.
    indelete = models.BooleanField(db_column='inDelete')  # Field name made lowercase.
    anomaly = models.BooleanField(blank=True, null=True)

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
    id = models.UUIDField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    status = models.BooleanField(blank=True, null=True)
    parent = models.UUIDField(blank=True, null=True)

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


class Scenarios(models.Model):
    id = models.UUIDField(primary_key=True)
    folder = models.UUIDField(blank=True, null=True)
    status = models.BooleanField()
    steps = models.ForeignKey('Steps', models.DO_NOTHING, db_column='steps', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenarios'


class Steps(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    idgadgets = models.TextField(blank=True, null=True)  # This field type is a guess.
    iduploading = models.ForeignKey('Uploading', models.DO_NOTHING, db_column='iduploading', blank=True, null=True)
    actionstep = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'steps'


class Uploading(models.Model):
    delete_id = models.IntegerField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    folder = models.UUIDField(blank=True, null=True)
    range = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    type_of_values = models.CharField(max_length=4, blank=True, null=True)
    type_of_uploading = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploading'
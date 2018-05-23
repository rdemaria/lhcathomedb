from peewee import *

lhcatohomedata = {'host': 'dbod-sixtrack.cern.ch',
                  'password': 'B01nclhc.',
                  'port': 5513, 'user':    'sixtadm'}
database = MySQLDatabase('sixt_production', **lhcatohomedata)

class UnknownField(object):
    def __init__(self, *_, **__):
        pass

class BaseModel(Model):
    class Meta:
        database = database
    def __repr__(self):
        out = ["%s("%self._meta.name]
        for field in self._meta.sorted_fields:
            name = field.name
            out.append("  %s= %s,"%(name, repr(getattr(self, name))))
        out.append(")")
        return '\n'.join(out)

class App(BaseModel):
    beta = IntegerField()
    create_time = IntegerField()
    deprecated = IntegerField()
    fraction_done_exact = IntegerField()
    homogeneous_app_version = IntegerField()
    homogeneous_redundancy = IntegerField()
    host_scale_check = IntegerField()
    locality_scheduling = IntegerField()
    min_avg_pfc = FloatField()
    min_version = IntegerField()
    n_size_classes = IntegerField()
    name = CharField(unique=True)
    non_cpu_intensive = IntegerField()
    target_nresults = IntegerField()
    user_friendly_name = CharField()
    weight = FloatField()

    class Meta:
        db_table = 'app'

class AppVersion(BaseModel):
    appid = IntegerField()
    beta = IntegerField()
    create_time = IntegerField()
    deprecated = IntegerField()
    expavg_credit = FloatField()
    expavg_time = FloatField()
    max_core_version = IntegerField()
    min_core_version = IntegerField()
    pfc_avg = FloatField()
    pfc_n = FloatField()
    pfc_scale = FloatField()
    plan_class = CharField()
    platformid = IntegerField()
    version_num = IntegerField()
    xml_doc = TextField(null=True)

    class Meta:
        db_table = 'app_version'
        indexes = (
            (('appid', 'platformid', 'version_num', 'plan_class'), True),
        )

class Assignment(BaseModel):
    create_time = IntegerField()
    multi = IntegerField()
    resultid = IntegerField()
    target = IntegerField(db_column='target_id')
    target_type = IntegerField()
    workunitid = IntegerField()

    class Meta:
        db_table = 'assignment'
        indexes = (
            (('target_type', 'target'), False),
        )

class Badge(BaseModel):
    create_time = FloatField()
    description = CharField()
    id = BigIntegerField(primary_key=True)
    image_url = CharField()
    level = CharField()
    name = CharField()
    sql_rule = CharField()
    tags = CharField()
    title = CharField()
    type = IntegerField()

    class Meta:
        db_table = 'badge'

class BadgeTeam(BaseModel):
    badge = IntegerField(db_column='badge_id')
    create_time = FloatField()
    reassign_time = FloatField()
    team = IntegerField(db_column='team_id')

    class Meta:
        db_table = 'badge_team'
        indexes = (
            (('team', 'badge'), True),
        )
        primary_key = False

class BadgeUser(BaseModel):
    badge = IntegerField(db_column='badge_id')
    create_time = FloatField()
    reassign_time = FloatField()
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'badge_user'
        indexes = (
            (('user', 'badge'), True),
        )
        primary_key = False

class BanishmentVote(BaseModel):
    end_time = IntegerField()
    id = BigIntegerField(primary_key=True)
    modid = IntegerField()
    start_time = IntegerField()
    userid = IntegerField()

    class Meta:
        db_table = 'banishment_vote'

class BanishmentVotes(BaseModel):
    id = BigIntegerField(primary_key=True)
    modid = IntegerField()
    time = IntegerField()
    voteid = IntegerField()
    yes = IntegerField()

    class Meta:
        db_table = 'banishment_votes'

class Batch(BaseModel):
    app = IntegerField(db_column='app_id')
    completion_time = FloatField()
    create_time = IntegerField()
    credit_canonical = FloatField()
    credit_estimate = FloatField()
    credit_total = FloatField()
    description = CharField()
    est_completion_time = FloatField()
    expire_time = FloatField()
    fraction_done = FloatField()
    id = BigIntegerField(primary_key=True)
    logical_end_time = FloatField()
    logical_start_time = FloatField()
    name = CharField()
    nerror_jobs = IntegerField()
    njobs = IntegerField()
    project_state = IntegerField()
    state = IntegerField()
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'batch'

class BatchFileAssoc(BaseModel):
    batch = IntegerField(db_column='batch_id')
    job_file = IntegerField(db_column='job_file_id')

    class Meta:
        db_table = 'batch_file_assoc'
        indexes = (
            (('job_file', 'batch'), True),
        )
        primary_key = False

class Category(BaseModel):
    is_helpdesk = IntegerField()
    lang = IntegerField()
    name = CharField(null=True)
    orderid = IntegerField(db_column='orderID')

    class Meta:
        db_table = 'category'
        indexes = (
            (('name', 'is_helpdesk'), True),
        )

class CreditMultiplier(BaseModel):
    appid = IntegerField()
    id = BigIntegerField(primary_key=True)
    multiplier = FloatField()
    time = IntegerField()

    class Meta:
        db_table = 'credit_multiplier'

class CreditTeam(BaseModel):
    appid = IntegerField()
    credit_type = IntegerField()
    expavg = FloatField()
    expavg_time = FloatField()
    njobs = IntegerField()
    teamid = IntegerField()
    total = FloatField()

    class Meta:
        db_table = 'credit_team'
        indexes = (
            (('appid', 'expavg'), False),
            (('appid', 'total'), False),
            (('teamid', 'appid', 'credit_type'), True),
        )
        primary_key = CompositeKey('appid', 'credit_type', 'teamid')

class CreditUser(BaseModel):
    appid = IntegerField()
    credit_type = IntegerField()
    expavg = FloatField()
    expavg_time = FloatField()
    njobs = IntegerField()
    total = FloatField()
    userid = IntegerField()

    class Meta:
        db_table = 'credit_user'
        indexes = (
            (('appid', 'expavg'), False),
            (('appid', 'total'), False),
            (('userid', 'appid', 'credit_type'), True),
        )
        primary_key = CompositeKey('appid', 'credit_type', 'userid')

class CreditedJob(BaseModel):
    userid = IntegerField(index=True)
    workunitid = BigIntegerField(index=True)

    class Meta:
        db_table = 'credited_job'
        indexes = (
            (('userid', 'workunitid'), True),
        )
        primary_key = False

class DonationItems(BaseModel):
    description = CharField()
    item_name = CharField()
    required = FloatField()
    title = CharField()

    class Meta:
        db_table = 'donation_items'

class DonationPaypal(BaseModel):
    email_addr = CharField()
    item_name = CharField()
    item_number = CharField()
    order_amount = FloatField()
    order_time = IntegerField()
    payer_email = CharField()
    payer_name = CharField()
    payment_amount = FloatField()
    payment_currency = CharField()
    payment_fee = FloatField(null=True)
    payment_status = CharField()
    payment_time = IntegerField()
    processed = IntegerField()
    receiver_email = CharField()
    txn = CharField(db_column='txn_id')
    userid = IntegerField()

    class Meta:
        db_table = 'donation_paypal'

class Forum(BaseModel):
    category = IntegerField()
    description = CharField()
    is_dev_blog = IntegerField()
    orderid = IntegerField(db_column='orderID')
    parent_type = IntegerField()
    post_min_expavg_credit = IntegerField()
    post_min_interval = IntegerField()
    post_min_total_credit = IntegerField()
    posts = IntegerField()
    rate_min_expavg_credit = IntegerField()
    rate_min_total_credit = IntegerField()
    threads = IntegerField()
    timestamp = IntegerField()
    title = CharField()

    class Meta:
        db_table = 'forum'
        indexes = (
            (('parent_type', 'category', 'title'), True),
        )

class ForumLogging(BaseModel):
    threadid = IntegerField()
    timestamp = IntegerField()
    userid = IntegerField()

    class Meta:
        db_table = 'forum_logging'
        indexes = (
            (('userid', 'threadid'), True),
        )
        primary_key = CompositeKey('threadid', 'userid')

class ForumPreferences(BaseModel):
    avatar = CharField()
    banished_until = IntegerField()
    display_wrap_postcount = IntegerField()
    forum_sorting = IntegerField()
    hide_avatars = IntegerField()
    hide_signatures = IntegerField()
    high_rating_threshold = IntegerField()
    highlight_special = IntegerField(null=True)
    ignore_sticky_posts = IntegerField()
    ignorelist = CharField()
    images_as_links = IntegerField()
    jump_to_unread = IntegerField()
    last_post = IntegerField()
    link_popup = IntegerField()
    low_rating_threshold = IntegerField()
    mark_as_read_timestamp = IntegerField()
    minimum_wrap_postcount = IntegerField()
    no_signature_by_default = IntegerField()
    pm_notification = IntegerField()
    posts = IntegerField()
    rated_posts = CharField()
    signature = CharField()
    special_user = CharField()
    thread_sorting = IntegerField()
    userid = PrimaryKeyField()

    class Meta:
        db_table = 'forum_preferences'

class Friend(BaseModel):
    create_time = IntegerField()
    message = CharField()
    reciprocated = IntegerField()
    user_dest = IntegerField()
    user_src = IntegerField()

    class Meta:
        db_table = 'friend'
        indexes = (
            (('user_src', 'user_dest'), True),
        )
        primary_key = False

class Host(BaseModel):
    active_frac = FloatField()
    avg_turnaround = FloatField()
    connected_frac = FloatField()
    cpu_efficiency = FloatField()
    create_time = IntegerField()
    credit_per_cpu_sec = FloatField()
    d_boinc_max = FloatField()
    d_boinc_used_project = FloatField()
    d_boinc_used_total = FloatField()
    d_free = FloatField()
    d_total = FloatField()
    domain_name = CharField(null=True)
    duration_correction_factor = FloatField()
    error_rate = FloatField()
    expavg_credit = FloatField(index=True)
    expavg_time = FloatField()
    external_ip_addr = CharField(null=True)
    gpu_active_frac = FloatField()
    host_cpid = CharField(null=True)
    last_ip_addr = CharField(null=True)
    m_cache = FloatField()
    m_nbytes = FloatField()
    m_swap = FloatField()
    max_results_day = IntegerField()
    n_bwdown = FloatField()
    n_bwup = FloatField()
    nresults_today = IntegerField()
    nsame_ip_addr = IntegerField()
    on_frac = FloatField()
    os_name = CharField(null=True)
    os_version = CharField(null=True)
    p_fpops = FloatField()
    p_iops = FloatField()
    p_membw = FloatField()
    p_model = CharField(null=True)
    p_ncpus = IntegerField()
    p_vendor = CharField(null=True)
    product_name = CharField()
    rpc_seqno = IntegerField()
    rpc_time = IntegerField()
    serialnum = CharField(null=True)
    timezone = IntegerField()
    total_credit = FloatField(index=True)
    userid = IntegerField(index=True)
    venue = CharField()

    class Meta:
        db_table = 'host'

class HostAppVersion(BaseModel):
    app_version = IntegerField(db_column='app_version_id')
    consecutive_valid = IntegerField()
    et_avg = FloatField()
    et_n = FloatField()
    et_q = FloatField()
    et_var = FloatField()
    host = IntegerField(db_column='host_id')
    max_jobs_per_day = IntegerField()
    n_jobs_today = IntegerField()
    pfc_avg = FloatField()
    pfc_n = FloatField()
    turnaround_avg = FloatField()
    turnaround_n = FloatField()
    turnaround_q = FloatField()
    turnaround_var = FloatField()

    class Meta:
        db_table = 'host_app_version'
        indexes = (
            (('host', 'app_version'), True),
        )
        primary_key = False

class JobFile(BaseModel):
    create_time = FloatField()
    delete_time = FloatField()
    md5 = CharField(index=True)

    class Meta:
        db_table = 'job_file'

class MsgFromHost(BaseModel):
    create_time = IntegerField()
    handled = IntegerField(index=True)
    hostid = IntegerField()
    variety = CharField()
    xml = TextField(null=True)

    class Meta:
        db_table = 'msg_from_host'

class MsgToHost(BaseModel):
    create_time = IntegerField()
    handled = IntegerField()
    hostid = IntegerField()
    variety = CharField()
    xml = TextField(null=True)

    class Meta:
        db_table = 'msg_to_host'
        indexes = (
            (('hostid', 'handled'), False),
        )

class Notify(BaseModel):
    create_time = IntegerField()
    id = BigIntegerField(primary_key=True)
    opaque = IntegerField()
    type = IntegerField()
    userid = IntegerField()

    class Meta:
        db_table = 'notify'
        indexes = (
            (('userid', 'type', 'opaque'), True),
        )

class Platform(BaseModel):
    create_time = IntegerField()
    deprecated = IntegerField()
    name = CharField(unique=True)
    user_friendly_name = CharField()

    class Meta:
        db_table = 'platform'

class Post(BaseModel):
    content = TextField(index=True)
    hidden = IntegerField()
    modified = IntegerField()
    parent_post = IntegerField()
    score = FloatField()
    signature = IntegerField()
    thread = IntegerField(index=True)
    timestamp = IntegerField()
    user = IntegerField(index=True)
    votes = IntegerField()

    class Meta:
        db_table = 'post'

class PostRatings(BaseModel):
    post = IntegerField()
    rating = IntegerField()
    user = IntegerField()

    class Meta:
        db_table = 'post_ratings'
        indexes = (
            (('post', 'user'), True),
        )
        primary_key = CompositeKey('post', 'user')

class PrivateMessages(BaseModel):
    content = TextField()
    date = IntegerField()
    opened = IntegerField()
    senderid = IntegerField()
    subject = CharField()
    userid = IntegerField(index=True)

    class Meta:
        db_table = 'private_messages'

class Profile(BaseModel):
    has_picture = IntegerField()
    language = CharField(null=True)
    posts = IntegerField()
    recommend = IntegerField()
    reject = IntegerField()
    response1 = TextField(null=True)
    response2 = TextField(null=True)
    uotd_time = IntegerField(index=True, null=True)
    userid = PrimaryKeyField()
    verification = IntegerField()

    class Meta:
        db_table = 'profile'
        indexes = (
            (('response1', 'response2'), False),
        )

class Result(BaseModel):
    app_version = IntegerField(db_column='app_version_id')
    app_version_num = IntegerField()
    appid = IntegerField()
    batch = IntegerField()
    claimed_credit = FloatField()
    client_state = IntegerField()
    cpu_time = FloatField()
    create_time = IntegerField()
    elapsed_time = FloatField()
    exit_status = IntegerField()
    file_delete_state = IntegerField(index=True)
    flops_estimate = FloatField()
    granted_credit = FloatField()
    hostid = IntegerField()
    mod_time = DateTimeField()
    name = CharField(unique=True)
    opaque = FloatField()
    outcome = IntegerField()
    peak_disk_usage = FloatField()
    peak_swap_size = FloatField()
    peak_working_set_size = FloatField()
    priority = IntegerField()
    random = IntegerField()
    received_time = IntegerField()
    report_deadline = IntegerField()
    runtime_outlier = IntegerField()
    sent_time = IntegerField()
    server_state = IntegerField()
    size_class = IntegerField()
    stderr_out = TextField(null=True)
    teamid = IntegerField()
    userid = IntegerField()
    validate_state = IntegerField()
    workunitid = IntegerField(index=True)
    xml_doc_in = TextField(null=True)
    xml_doc_out = TextField(null=True)

    class Meta:
        db_table = 'result'
        indexes = (
            (('appid', 'server_state'), False),
            (('hostid', 'id'), False),
            (('server_state', 'priority'), False),
            (('userid', 'id'), False),
            (('userid', 'validate_state'), False),
            (('workunitid', 'userid'), False),
        )

class SentEmail(BaseModel):
    email_type = IntegerField()
    time_sent = IntegerField()
    userid = PrimaryKeyField()

    class Meta:
        db_table = 'sent_email'

class StateCounts(BaseModel):
    appid = PrimaryKeyField()
    last_update_time = IntegerField()
    result_file_delete_state_1 = IntegerField()
    result_file_delete_state_2 = IntegerField()
    result_server_state_2 = IntegerField()
    result_server_state_4 = IntegerField()
    result_server_state_5_and_file_delete_state_0 = IntegerField()
    workunit_assimilate_state_1 = IntegerField()
    workunit_file_delete_state_1 = IntegerField()
    workunit_file_delete_state_2 = IntegerField()
    workunit_need_validate_1 = IntegerField()

    class Meta:
        db_table = 'state_counts'

class Subscriptions(BaseModel):
    notified_time = IntegerField()
    threadid = IntegerField()
    userid = IntegerField()

    class Meta:
        db_table = 'subscriptions'
        indexes = (
            (('userid', 'threadid'), True),
        )
        primary_key = False

class Team(BaseModel):
    country = CharField(null=True)
    create_time = IntegerField()
    description = TextField(null=True)
    expavg_credit = FloatField(index=True)
    expavg_time = FloatField()
    joinable = IntegerField()
    name = CharField(index=True)
    name_html = CharField(null=True)
    name_lc = CharField(null=True)
    nusers = IntegerField()
    ping_time = IntegerField()
    ping_user = IntegerField()
    seti = IntegerField(db_column='seti_id')
    total_credit = FloatField(index=True)
    type = IntegerField()
    url = CharField(null=True)
    userid = IntegerField(index=True)

    class Meta:
        db_table = 'team'
        indexes = (
            (('name', 'description'), False),
        )

class TeamAdmin(BaseModel):
    create_time = IntegerField()
    rights = IntegerField()
    teamid = IntegerField()
    userid = IntegerField()

    class Meta:
        db_table = 'team_admin'
        indexes = (
            (('teamid', 'userid'), True),
        )
        primary_key = False

class TeamDelta(BaseModel):
    joining = IntegerField()
    teamid = IntegerField()
    timestamp = IntegerField()
    total_credit = FloatField()
    userid = IntegerField()

    class Meta:
        db_table = 'team_delta'
        indexes = (
            (('teamid', 'timestamp'), False),
        )
        primary_key = False

class Thread(BaseModel):
    activity = FloatField()
    create_time = IntegerField()
    forum = IntegerField()
    hidden = IntegerField()
    locked = IntegerField()
    owner = IntegerField()
    replies = IntegerField()
    score = FloatField()
    status = IntegerField()
    sticky = IntegerField()
    sufferers = IntegerField()
    timestamp = IntegerField()
    title = CharField(index=True)
    views = IntegerField()
    votes = IntegerField()

    class Meta:
        db_table = 'thread'

class User(BaseModel):
    authenticator = CharField(null=True, unique=True)
    country = CharField(null=True)
    create_time = IntegerField()
    cross_project = CharField(db_column='cross_project_id')
    donated = IntegerField()
    email_addr = CharField(unique=True)
    email_validated = IntegerField()
    expavg_credit = FloatField(index=True)
    expavg_time = FloatField()
    global_prefs = TextField(null=True)
    has_profile = IntegerField()
    name = CharField(index=True, null=True)
    passwd_hash = CharField()
    postal_code = CharField(null=True)
    posts = IntegerField()
    project_prefs = TextField(null=True)
    send_email = IntegerField()
    seti = IntegerField(db_column='seti_id')
    seti_last_result_time = IntegerField()
    seti_nresults = IntegerField()
    seti_total_cpu = FloatField()
    show_hosts = IntegerField()
    signature = CharField(null=True)
    teamid = IntegerField(index=True)
    total_credit = FloatField(index=True)
    url = CharField(null=True)
    venue = CharField()

    class Meta:
        db_table = 'user'

class UserSubmit(BaseModel):
    create_app_versions = IntegerField()
    create_apps = IntegerField()
    logical_start_time = FloatField()
    manage_all = IntegerField()
    max_jobs_in_progress = IntegerField()
    quota = FloatField()
    submit_all = IntegerField()
    user = PrimaryKeyField(db_column='user_id')

    class Meta:
        db_table = 'user_submit'

class UserSubmitApp(BaseModel):
    app = IntegerField(db_column='app_id')
    manage = IntegerField()
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'user_submit_app'
        indexes = (
            (('user', 'app'), True),
        )
        primary_key = CompositeKey('app', 'user')

class Workunit(BaseModel):
    app_version = IntegerField(db_column='app_version_id')
    appid = IntegerField()
    assimilate_state = IntegerField()
    batch = IntegerField(index=True)
    canonical_credit = FloatField()
    canonical_resultid = IntegerField()
    create_time = IntegerField()
    delay_bound = IntegerField()
    error_mask = IntegerField()
    file_delete_state = IntegerField(index=True)
    fileset = IntegerField(db_column='fileset_id')
    hr_class = IntegerField()
    max_error_results = IntegerField()
    max_success_results = IntegerField()
    max_total_results = IntegerField()
    min_quorum = IntegerField()
    mod_time = DateTimeField()
    name = CharField(unique=True)
    need_validate = IntegerField()
    opaque = FloatField()
    priority = IntegerField()
    result_template_file = CharField()
    rsc_bandwidth_bound = FloatField()
    rsc_disk_bound = FloatField()
    rsc_fpops_bound = FloatField()
    rsc_fpops_est = FloatField()
    rsc_memory_bound = FloatField()
    size_class = IntegerField()
    target_nresults = IntegerField()
    transition_time = IntegerField(index=True)
    transitioner_flags = IntegerField()
    xml_doc = TextField(null=True)

    class Meta:
        db_table = 'workunit'
        indexes = (
            (('appid', 'assimilate_state'), False),
            (('appid', 'need_validate'), False),
        )


from dotenv import load_dotenv
import os
from pytest import fixture
import vcr

from kb4 import KnowBe4

load_dotenv()
KB4_API_KEY = os.environ.get('KB4_API_KEY', None)


@fixture
def account_info():
    return [
        'name',
        'type',
        'domains',
        'admins',
        'subscription_level',
        'subscription_end_date',
        'number_of_seats',
        'current_risk_score',
        'risk_score_history'
    ]


@fixture
def users_info():
    return [
        'id',
        'employee_number',
        'first_name',
        'last_name',
        'job_title',
        'email',
        'phish_prone_percentage',
        'phone_number',
        'extension',
        'mobile_phone_number',
        'location',
        'division',
        'manager_name',
        'manager_email',
        'adi_manageable',
        'adi_guid',
        'groups',
        'aliases',
        'joined_on',
        'last_sign_in',
        'status',
        'organization',
        'department',
        'language',
        'comment',
        'employee_start_date',
        'archived_at',
        'custom_field_1',
        'custom_field_2',
        'custom_field_3',
        'custom_field_4',
        'custom_date_1',
        'custom_date_2'
    ]


@fixture
def group_members_info():
    return [
        'id',
        'employee_number',
        'first_name',
        'last_name',
        'job_title',
        'email',
        'phish_prone_percentage',
        'phone_number',
        'extension',
        'mobile_phone_number',
        'location',
        'division',
        'manager_name',
        'manager_email',
        'adi_manageable',
        'adi_guid',
        'groups',
        'aliases',
        'joined_on',
        'last_sign_in',
        'status',
        'organization',
        'department',
        'language',
        'comment',
        'employee_start_date',
        'archived_at',
        'custom_field_1',
        'custom_field_2',
        'custom_field_3',
        'custom_field_4',
        'custom_date_1',
        'custom_date_2'
    ]


@fixture
def user_info():
    return [
        'id',
        'employee_number',
        'first_name',
        'last_name',
        'job_title',
        'email',
        'phish_prone_percentage',
        'phone_number',
        'extension',
        'mobile_phone_number',
        'location',
        'division',
        'manager_name',
        'manager_email',
        'adi_manageable',
        'adi_guid',
        'groups',
        'aliases',
        'joined_on',
        'last_sign_in',
        'status',
        'organization',
        'department',
        'language',
        'comment',
        'employee_start_date',
        'archived_at',
        'custom_field_1',
        'custom_field_2',
        'custom_field_3',
        'custom_field_4',
        'custom_date_1',
        'custom_date_2'
    ]


@fixture
def groups_info():
    return [
        'id',
        'name',
        'group_type',
        'adi_guid',
        'member_count',
        'status'
    ]


@fixture
def group_info():
    return [
        'id',
        'name',
        'group_type',
        'adi_guid',
        'member_count',
        'status'
    ]


@fixture
def phishing_campaigns_info():
    return [
        'campaign_id',
        'name',
        'groups',
        'last_phish_prone_percentage',
        'last_run',
        'status',
        'hidden',
        'send_duration',
        'track_duration',
        'frequency',
        'difficulty_filter',
        'create_date',
        'psts_count',
        'psts'
    ]


@fixture
def phishing_campaign_info():
    return [
        'campaign_id',
        'name',
        'groups',
        'last_phish_prone_percentage',
        'last_run',
        'status',
        'hidden',
        'send_duration',
        'track_duration',
        'frequency',
        'difficulty_filter',
        'create_date',
        'psts_count',
        'psts'
    ]


@fixture
def phishing_security_tests_info():
    return [
        'campaign_id',
        'pst_id',
        'status',
        'name',
        'groups',
        'phish_prone_percentage',
        'started_at',
        'duration',
        'categories',
        'template',
        'landing_page',
        'scheduled_count',
        'delivered_count',
        'opened_count',
        'clicked_count',
        'replied_count',
        'attachment_open_count',
        'macro_enabled_count',
        'data_entered_count',
        'vulnerable_plugin_count',
        'exploited_count',
        'reported_count',
        'bounced_count'
    ]


@fixture
def phishing_campaign_security_tests_info():
    return [
        'campaign_id',
        'pst_id',
        'status',
        'name',
        'groups',
        'phish_prone_percentage',
        'started_at',
        'duration',
        'categories',
        'template',
        'landing_page',
        'scheduled_count',
        'delivered_count',
        'opened_count',
        'clicked_count',
        'replied_count',
        'attachment_open_count',
        'macro_enabled_count',
        'data_entered_count',
        'vulnerable_plugin_count',
        'exploited_count',
        'reported_count',
        'bounced_count'
    ]


@fixture
def phishing_campaign_security_test_info():
    return [
        'campaign_id',
        'pst_id',
        'status',
        'name',
        'groups',
        'phish_prone_percentage',
        'started_at',
        'duration',
        'categories',
        'template',
        'landing_page',
        'scheduled_count',
        'delivered_count',
        'opened_count',
        'clicked_count',
        'replied_count',
        'attachment_open_count',
        'macro_enabled_count',
        'data_entered_count',
        'vulnerable_plugin_count',
        'exploited_count',
        'reported_count',
        'bounced_count'
    ]


@fixture
def phishing_campaign_security_test_recipients_info():
    return [
        'recipient_id',
        'pst_id',
        'user',
        'template',
        'scheduled_at',
        'delivered_at',
        'opened_at',
        'clicked_at',
        'replied_at',
        'attachment_opened_at',
        'macro_enabled_at',
        'data_entered_at',
        'vulnerable_plugins_at',
        'exploited_at',
        'reported_at',
        'bounced_at',
        'ip',
        'ip_location',
        'browser',
        'browser_version',
        'os'
    ]


@fixture
def phishing_campaign_security_test_recipient_info():
    return [
        'recipient_id',
        'pst_id',
        'user',
        'template',
        'scheduled_at',
        'delivered_at',
        'opened_at',
        'clicked_at',
        'replied_at',
        'attachment_opened_at',
        'macro_enabled_at',
        'data_entered_at',
        'vulnerable_plugins_at',
        'exploited_at',
        'reported_at',
        'bounced_at',
        'ip',
        'ip_location',
        'browser',
        'browser_version',
        'os'
    ]


@fixture
def store_purchases_info():
    return [
        'store_purchase_id',
        'content_type',
        'name',
        'description',
        'type',
        'duration',
        'retired',
        'retirement_date',
        'publish_date',
        'publisher',
        'purchase_date',
        'policy_url'
    ]


@fixture
def store_purchase_info():
    return [
        'store_purchase_id',
        'content_type',
        'name',
        'description',
        'type',
        'duration',
        'retired',
        'retirement_date',
        'publish_date',
        'publisher',
        'purchase_date',
        'policy_url'
    ]


@fixture
def policies_info():
    return [
        'policy_id',
        'name',
        'content_type',
        'minimum_time',
        'default_language',
        'published'
    ]


@fixture
def policy_info():
    return [
        'policy_id',
        'name',
        'content_type',
        'minimum_time',
        'default_language',
        'published'
    ]


@fixture
def training_campaigns_info():
    return [
        'campaign_id',
        'name',
        'groups',
        'status',
        'modules',
        'content',
        'duration_type',
        'start_date',
        'end_date',
        'relative_duration',
        'auto_enroll',
        'allow_multiple_enrollments'
    ]


@fixture
def training_campaign_info():
    return [
        'campaign_id',
        'name',
        'groups',
        'status',
        'modules',
        'content',
        'duration_type',
        'start_date',
        'end_date',
        'relative_duration',
        'auto_enroll',
        'allow_multiple_enrollments'
    ]


@fixture
def training_enrollments_info():
    return [
        'enrollment_id',
        'module_name',
        'content_type',
        'user',
        'campaign_name',
        'enrollment_date',
        'start_date',
        'completion_date',
        'status',
        'time_spent',
        'policy_acknowledged'
    ]


@fixture
def training_enrollment_info():
    return [
        'enrollment_id',
        'module_name',
        'content_type',
        'user',
        'campaign_name',
        'enrollment_date',
        'start_date',
        'completion_date',
        'status',
        'time_spent',
        'policy_acknowledged'
    ]


@vcr.use_cassette('tests/cassettes/account_info.yml')
def test_account_info(account_info):
    """Tests an API call to get KnowBe4 account info."""

    kb4 = KnowBe4(KB4_API_KEY).account()

    assert isinstance(kb4, dict)
    assert set(account_info).issubset(
        kb4.keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/users_info.yml')
def test_users_info(users_info):
    """Tests an API call to get KnowBe4 user info."""

    kb4 = KnowBe4(KB4_API_KEY).users()

    assert isinstance(kb4, list)
    assert set(users_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/group_members_info.yml')
def test_group_members_info(group_members_info):

    kb4 = KnowBe4(KB4_API_KEY).group_members(409606)

    assert isinstance(kb4, list)
    assert set(group_members_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/user_info.yml')
def test_user_info(user_info):

    kb4 = KnowBe4(KB4_API_KEY).user(8640689)

    assert isinstance(kb4, dict)
    assert set(user_info).issubset(
        kb4.keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/groups_info.yml')
def test_groups_info(groups_info):

    kb4 = KnowBe4(KB4_API_KEY).groups()

    assert isinstance(kb4, list)
    assert set(groups_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/group_info.yml')
def test_group_info(group_info):

    kb4 = KnowBe4(KB4_API_KEY).group(411997)

    assert isinstance(kb4, dict)
    assert set(group_info).issubset(
        kb4.keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/phishing_campaigns_info.yml')
def test_phishing_campaigns_info(phishing_campaigns_info):

    kb4 = KnowBe4(KB4_API_KEY).phishing_campaigns()

    assert isinstance(kb4, list)
    assert set(phishing_campaigns_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/phishing_campaign_info.yml')
def test_phishing_campaign_info(phishing_campaign_info):

    kb4 = KnowBe4(KB4_API_KEY).phishing_campaign(370772)

    assert isinstance(kb4, dict)
    assert set(phishing_campaign_info).issubset(
        kb4.keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/phishing_security_tests_info.yml')
def test_phishing_security_tests_info(phishing_security_tests_info):

    kb4 = KnowBe4(KB4_API_KEY).phishing_security_tests()

    assert isinstance(kb4, list)
    assert set(phishing_security_tests_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/phishing_campaign_security_tests_info.yml')
def test_phishing_campaign_security_tests_info(phishing_campaign_security_tests_info):

    kb4 = KnowBe4(KB4_API_KEY).phishing_campaign_security_tests(370772)

    assert isinstance(kb4, list)
    assert set(phishing_campaign_security_tests_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/phishing_campaign_security_test_info.yml')
def test_phishing_campaign_security_test_info(phishing_campaign_security_test_info):

    kb4 = KnowBe4(KB4_API_KEY).phishing_campaign_security_test(1962421)

    assert isinstance(kb4, dict)
    assert set(phishing_campaign_security_test_info).issubset(
        kb4.keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/phishing_campaign_security_test_recipients_info.yml')
def test_phishing_campaign_security_test_recipients_info(phishing_campaign_security_test_recipients_info):

    kb4 = KnowBe4(
        KB4_API_KEY).phishing_campaign_security_test_recipients(1962421)

    assert isinstance(kb4, list)
    assert set(phishing_campaign_security_test_recipients_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/phishing_campaign_security_test_recipient_info.yml')
def test_phishing_campaign_security_test_recipient_info(phishing_campaign_security_test_recipient_info):

    kb4 = KnowBe4(KB4_API_KEY).phishing_campaign_security_test_recipient(
        1962421, 447217478)

    assert isinstance(kb4, dict)
    assert set(phishing_campaign_security_test_recipient_info).issubset(
        kb4.keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/store_purchases_info.yml')
def test_store_purchases_info(store_purchases_info):

    kb4 = KnowBe4(KB4_API_KEY).store_purchases()

    assert isinstance(kb4, list)
    assert set(store_purchases_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/store_purchase_info.yml')
def test_store_purchase_info(store_purchase_info):

    kb4 = KnowBe4(KB4_API_KEY).store_purchase(1263386)

    assert isinstance(kb4, dict)
    assert set(store_purchase_info).issubset(
        kb4.keys()), "All keys should be in the response"


'''
@vcr.use_cassette('tests/cassettes/policies_info.yml')
def test_policies_info(policies_info):

    kb4 = KnowBe4(KB4_API_KEY).policies()

    assert isinstance(kb4, list)
    assert set(policies_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/policy_info.yml')
def test_policy_info(policy_info):

    kb4 = KnowBe4(KB4_API_KEY).policy()

    assert isinstance(kb4, dict)
    assert set(policies_info).issubset(
        kb4.keys()), "All keys should be in the response"
'''


@vcr.use_cassette('tests/cassettes/training_campaigns_info.yml')
def test_training_campaigns_info(training_campaigns_info):

    kb4 = KnowBe4(KB4_API_KEY).training_campaigns()

    assert isinstance(kb4, list)
    assert set(training_campaigns_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/training_campaign_info.yml')
def test_training_campaign_info(training_campaign_info):

    kb4 = KnowBe4(KB4_API_KEY).training_campaign(148519)

    assert isinstance(kb4, dict)
    assert set(training_campaign_info).issubset(
        kb4.keys()), "All keys should be in the response"


'''
@vcr.use_cassette('tests/cassettes/training_enrollments_info.yml')
def test_training_enrollments_info(training_enrollments_info):

    kb4 = KnowBe4(KB4_API_KEY).training_enrollments()

    assert isinstance(kb4, list)
    assert set(training_enrollments_info).issubset(
        kb4[0].keys()), "All keys should be in the response"


@vcr.use_cassette('tests/cassettes/training_enrollment_info.yml')
def test_training_enrollment_info(training_enrollment_info):

    kb4 = KnowBe4(KB4_API_KEY).training_enrollment()

    assert isinstance(kb4, dict)
    assert set(training_enrollment_info).issubset(
        kb4.keys()), "All keys should be in the response"
'''

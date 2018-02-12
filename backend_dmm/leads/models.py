from enum import Enum

from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField


class Lead(models.Model):
    """Collect data about a lead."""

    email = models.EmailField(max_length=120, unique=True)
    name = models.CharField(max_length=50, blank=True)
    phone = PhoneNumberField()
    message = models.CharField(max_length=1000, blank=True)
    comment = models.CharField(max_length=500, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'lead'
        verbose_name_plural = 'leads'
        ordering = ('-date',)


class Brief(models.Model):
    """Collect brief data."""

    class INDUSTRIES(Enum):
        forex = ('fx', 'Forex')
        binary = ('bn', 'Binary')
        ico = ('ico', 'ICO')
        cloud_mining = ('cm', 'Cloud Mining')
        online_games = ('og', 'Online Games')
        other = ('o', 'Other')

    class EXPERIENCE(Enum):
        less_1 = ('ls_1', 'Up to 1 year')
        less_3 = ('ls_3', 'From 1 to 3 years')
        more_3 = ('mr_3', 'More than 3 years')
        no_experience = ('n_ex', 'I want to found a startup and '
                         'I don’t have experience')

    class AIMS(Enum):
        new_project = ('new', 'Create a new turn-key project from scratch ')
        marketing = ('mk', 'Create a general marketing strategy for '
                     'my project')
        payment = ('pt', 'Connect the optimal payment system for my project')
        leads = ('ld', 'Increase the number of leads for my project')
        brand = ('brd', 'Strengthen brand by increasing audience coverage')
        other = ('o', 'Other')

    class STAGES(Enum):
        beginner = ('bg', "I'm beginner and have no results yet")
        preparing = ('prep', 'I passed the preparatory stage and I plan '
                     'to start active attracting clients')
        started = ('st', 'All necessary directions of my business are '
                   'created and started')
        improvement = ('imp', 'Everything works perfectly, but I want '
                       'a point improvement of some processes')
        other = ('o', 'Other')

    class STRATEGIES(Enum):
        strong = ('stg', 'The development strategy is strong and was '
                  'adjusted a minimum number of times')
        no_strategy = ('no_s', 'I have no strategy, I act through '
                       'the way of trial and error')
        considered = ('cs', 'The main activity is considered to the detail '
                      'but at some points I don’t have the right planning')
        situational = ('sit', 'In my opinion, my approach is situational. '
                       'It is extremely difficult to build a long-term '
                       'strategy of actions')
        other = ('o', 'Other')

    class AUDIENCES(Enum):
        small_country = ('sm_c', 'Small group in one of the countries')
        large_country = ('lg_c', 'Broad coverage in one country')
        small_international = ('sm_i', 'Limited audience in several '
                               'countries')
        large_international = ('lg_i', 'Large audience in several countries')
        other = ('o', 'Other')

    class CALLCENTERS(Enum):
        own_callcenter = ('own', 'I have/plan to create my own call center')
        outsourced_callcenter = ('ots', 'I use / plan to use outsourced call '
                                 'center')
        messaging = ('msg', 'I replace the call center with messaging or '
                     'chatting')
        robots = ('rb', 'The process of communication with customers is '
                  'robotized')
        no_callcenter = ('no_c', 'I don’t see the need to create a call '
                         'center')
        other = ('o', 'Other')

    class MARKETING(Enum):
        own = ('own', 'Yes, we develop/plan to develop all the necessary '
               'creatives ourselves')
        freelance = ('fr', 'No, we order advertisement at advertising '
                     'agencies or freelancers')
        contract = ('co', 'We plan our activity for a long-term and order '
                    'all advertising support on a contract basis, following '
                    'the brand-book and the general strategy')
        other = ('o', 'Other')

    class PAYMENTS(Enum):
        cards = ('cd', 'Bank cards')
        transfers = ('tsf', 'Bank Transfer')
        ewallets = ('wl', 'E-Wallet')
        crypto = ('cr', 'Cryptocurrency')
        other = ('o', 'Other')

    industry = models.CharField(
                    max_length=4,
                    choices=[x.value for x in INDUSTRIES])
    experience = models.CharField(
                    max_length=4,
                    choices=[x.value for x in EXPERIENCE])
    aim = models.CharField(
                    max_length=4,
                    choices=[x.value for x in AIMS])
    stage = models.CharField(
                    max_length=4,
                    choices=[x.value for x in STAGES])
    strategies = models.CharField(
                    max_length=4,
                    choices=[x.value for x in STRATEGIES])
    audience = models.CharField(
                    max_length=4,
                    choices=[x.value for x in AUDIENCES])
    callcenter = models.CharField(
                    max_length=4,
                    choices=[x.value for x in CALLCENTERS])
    marketing = models.CharField(
                    max_length=4,
                    choices=[x.value for x in MARKETING])
    payment = models.CharField(
                    max_length=4,
                    choices=[x.value for x in PAYMENTS])

    date = models.DateTimeField(default=timezone.now)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE,
                             related_name='brief')

    def __str__(self):
        return f'Brief of {self.lead.email}'

    class Meta:
        verbose_name = 'brief'
        verbose_name_plural = 'briefs'
        ordering = ('-date',)

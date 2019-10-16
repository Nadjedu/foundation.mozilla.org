# Generated by Django 2.2.5 on 2019-10-01 21:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0085_youtuberegretspage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuberegretspage',
            name='regret_stories',
            field=wagtail.core.fields.StreamField([('regret_story', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(help_text='Headline of this YouTube Regret')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('imageAltText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=False)), ('story', wagtail.core.blocks.TextBlock(help_text='Story of this YouTube Regret', verbose_name='youtube_regret_story'))]))]),
        ),
        migrations.AlterField(
            model_name='youtuberegretspage',
            name='regret_stories_de',
            field=wagtail.core.fields.StreamField([('regret_story', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(help_text='Headline of this YouTube Regret')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('imageAltText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=False)), ('story', wagtail.core.blocks.TextBlock(help_text='Story of this YouTube Regret', verbose_name='youtube_regret_story'))]))], null=True),
        ),
        migrations.AlterField(
            model_name='youtuberegretspage',
            name='regret_stories_en',
            field=wagtail.core.fields.StreamField([('regret_story', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(help_text='Headline of this YouTube Regret')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('imageAltText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=False)), ('story', wagtail.core.blocks.TextBlock(help_text='Story of this YouTube Regret', verbose_name='youtube_regret_story'))]))], null=True),
        ),
        migrations.AlterField(
            model_name='youtuberegretspage',
            name='regret_stories_es',
            field=wagtail.core.fields.StreamField([('regret_story', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(help_text='Headline of this YouTube Regret')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('imageAltText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=False)), ('story', wagtail.core.blocks.TextBlock(help_text='Story of this YouTube Regret', verbose_name='youtube_regret_story'))]))], null=True),
        ),
        migrations.AlterField(
            model_name='youtuberegretspage',
            name='regret_stories_fr',
            field=wagtail.core.fields.StreamField([('regret_story', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(help_text='Headline of this YouTube Regret')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('imageAltText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=False)), ('story', wagtail.core.blocks.TextBlock(help_text='Story of this YouTube Regret', verbose_name='youtube_regret_story'))]))], null=True),
        ),
        migrations.AlterField(
            model_name='youtuberegretspage',
            name='regret_stories_pl',
            field=wagtail.core.fields.StreamField([('regret_story', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(help_text='Headline of this YouTube Regret')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('imageAltText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=False)), ('story', wagtail.core.blocks.TextBlock(help_text='Story of this YouTube Regret', verbose_name='youtube_regret_story'))]))], null=True),
        ),
        migrations.AlterField(
            model_name='youtuberegretspage',
            name='regret_stories_pt',
            field=wagtail.core.fields.StreamField([('regret_story', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(help_text='Headline of this YouTube Regret')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('imageAltText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=False)), ('story', wagtail.core.blocks.TextBlock(help_text='Story of this YouTube Regret', verbose_name='youtube_regret_story'))]))], null=True),
        ),
    ]
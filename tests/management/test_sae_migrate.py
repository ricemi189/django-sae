# coding=utf-8
from django_sae.management.commands import sae_migrate
from .base import CommandTestBase


class SaeMigrateTestCase(CommandTestBase):
    def test_command(self):
        command = sae_migrate.Command()
        self.execute(command, db_dry_run=True, verbosity=2)  # verbosity大于1，则打印详细信息



"""Flask WTForm models."""

from flask_wtf import Form

from wtforms import (
    SelectField,
    TextField,
)
from wtforms.validators import DataRequired

import models


class ProspectorResultsForm(Form):
    """A form for generating results from the prospector analysis tool."""

    strictness = SelectField(
        u'Strictness level',
        choices=models.enum2list(models.Strictness),
        validators=[DataRequired()])
    output = SelectField(
        u'Output format',
        choices=models.enum2list(models.OutputFormat),
        validators=[DataRequired()],
    )
    path = TextField(u'Filepath (e.g. ./foo/bar.py)',
                     validators=[DataRequired()])

    def validate_path(self, field):
        """Validate file path name."""
        # Folders are ok
        if '.' in field.data:
            # Python ending files only.
            if not field.data.endswith('.py'):
                raise ValueError('Only python files are allowed.')

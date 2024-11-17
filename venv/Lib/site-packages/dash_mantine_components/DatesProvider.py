# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DatesProvider(Component):
    """A DatesProvider component.
esProvider

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- settings (dict; required)

    `settings` is a dict with keys:

    - locale (string; optional)

    - timezone (string; optional)

    - firstDayOfWeek (a value equal to: 0, 1, 2, 3, 4, 5, 6; optional)

    - weekendDays (list of a value equal to: 0, 1, 2, 3, 4, 5, 6s; optional)

    - labelSeparator (string; optional)

    - consistentWeeks (boolean; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'DatesProvider'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, settings=Component.REQUIRED, **kwargs):
        self._prop_names = ['children', 'id', 'settings']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'settings']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['settings']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DatesProvider, self).__init__(children=children, **args)

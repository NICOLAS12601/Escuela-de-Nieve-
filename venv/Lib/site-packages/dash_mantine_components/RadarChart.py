# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class RadarChart(Component):
    """A RadarChart component.
arChart

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Additional components that are rendered inside recharts
    `RadarChart` component.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- aria-* (string; optional):
    Wild card aria attributes.

- bd (string | number; optional):
    Border.

- bg (boolean | number | string | dict | list; optional):
    Background, theme key: theme.colors.

- bga (boolean | number | string | dict | list; optional):
    BackgroundAttachment.

- bgp (string | number; optional):
    BackgroundPosition.

- bgr (boolean | number | string | dict | list; optional):
    BackgroundRepeat.

- bgsz (string | number; optional):
    BackgroundSize.

- bottom (string | number; optional)

- c (boolean | number | string | dict | list; optional):
    Color.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- clickData (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Click data.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data (list of dicts with strings as keys and values of type boolean | number | string | dict | list; required):
    Data used in the chart.

- data-* (string; optional):
    Wild card data attributes.

- dataKey (string; required):
    Key of the `data` object for axis values.

- display (boolean | number | string | dict | list; optional)

- ff (boolean | number | string | dict | list; optional):
    FontFamily.

- flex (string | number; optional)

- fs (boolean | number | string | dict | list; optional):
    FontStyle.

- fw (boolean | number | string | dict | list; optional):
    FontWeight.

- fz (number; optional):
    FontSize, theme key: theme.fontSizes.

- gridColor (boolean | number | string | dict | list; optional):
    Controls color of the grid lines. By default, color depends on the
    color scheme.

- h (string | number; optional):
    Height, theme key: theme.spacing.

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- inset (string | number; optional)

- left (string | number; optional)

- legendProps (dict; optional):
    Props passed down to recharts Legend component.

- lh (number; optional):
    LineHeight, theme key: lineHeights.

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - is_loading (boolean; required):
        Determines if the component is loading or not.

    - prop_name (string; required):
        Holds which property is loading.

    - component_name (string; required):
        Holds the name of the component that is loading.

- lts (string | number; optional):
    LetterSpacing.

- m (number; optional):
    Margin, theme key: theme.spacing.

- mah (string | number; optional):
    MaxHeight, theme key: theme.spacing.

- maw (string | number; optional):
    MaxWidth, theme key: theme.spacing.

- mb (number; optional):
    MarginBottom, theme key: theme.spacing.

- me (number; optional):
    MarginInlineEnd, theme key: theme.spacing.

- mih (string | number; optional):
    MinHeight, theme key: theme.spacing.

- miw (string | number; optional):
    MinWidth, theme key: theme.spacing.

- ml (number; optional):
    MarginLeft, theme key: theme.spacing.

- mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Element modifiers transformed into `data-` attributes, for
    example, `{ 'data-size': 'xl' }`, falsy values are removed.

- mr (number; optional):
    MarginRight, theme key: theme.spacing.

- ms (number; optional):
    MarginInlineStart, theme key: theme.spacing.

- mt (number; optional):
    MarginTop, theme key: theme.spacing.

- mx (number; optional):
    MarginInline, theme key: theme.spacing.

- my (number; optional):
    MarginBlock, theme key: theme.spacing.

- opacity (boolean | number | string | dict | list; optional)

- p (number; optional):
    Padding, theme key: theme.spacing.

- pb (number; optional):
    PaddingBottom, theme key: theme.spacing.

- pe (number; optional):
    PaddingInlineEnd, theme key: theme.spacing.

- pl (number; optional):
    PaddingLeft, theme key: theme.spacing.

- polarAngleAxisProps (dict; optional):
    Props passed down to recharts PolarAngleAxis component.

- polarGridProps (dict; optional):
    Props passed down to recharts PolarGrid component.

- polarRadiusAxisProps (dict; optional):
    Props passed down to recharts PolarRadiusAxis component.

- pos (boolean | number | string | dict | list; optional):
    Position.

- pr (number; optional):
    PaddingRight, theme key: theme.spacing.

- ps (number; optional):
    PaddingInlineStart, theme key: theme.spacing.

- pt (number; optional):
    PaddingTop, theme key: theme.spacing.

- px (number; optional):
    PaddingInline, theme key: theme.spacing.

- py (number; optional):
    PaddingBlock, theme key: theme.spacing.

- radarChartProps (dict; optional):
    Props passed down to recharts RadarChart component.

- radarProps (boolean | number | string | dict | list; optional):
    Props passed down to recharts Radar component in a dict.

- right (string | number; optional)

- series (list of dicts; required):
    Determines which data should be consumed from the `data` array.

    `series` is a list of dicts with keys:

    - name (string; required)

    - color (boolean | number | string | dict | list; required)

    - strokeColor (boolean | number | string | dict | list; optional)

    - opacity (number; optional)

- style (optional):
    Inline style added to root component element, can subscribe to
    theme defined on MantineProvider.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (boolean | number | string | dict | list; optional):
    TextAlign.

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional):
    TextDecoration.

- textColor (boolean | number | string | dict | list; optional):
    Controls color of all text elements. By default, color depends on
    the color scheme.

- top (string | number; optional)

- tt (boolean | number | string | dict | list; optional):
    TextTransform.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional):
    Width, theme key: theme.spacing.

- withLegend (boolean; optional):
    Determines whether chart legend should be displayed, `False` by
    default.

- withPolarAngleAxis (boolean; optional):
    Determines whether PolarAngleAxis component should be displayed,
    `True` by default.

- withPolarGrid (boolean; optional):
    Determines whether PolarGrid component should be displayed, `True`
    by default.

- withPolarRadiusAxis (boolean; optional):
    Determines whether PolarRadiusAxisProps component should be
    displayed, `False` by default."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'RadarChart'
    @_explicitize_args
    def __init__(self, children=None, data=Component.REQUIRED, series=Component.REQUIRED, dataKey=Component.REQUIRED, gridColor=Component.UNDEFINED, legendProps=Component.UNDEFINED, textColor=Component.UNDEFINED, withLegend=Component.UNDEFINED, withPolarGrid=Component.UNDEFINED, withPolarAngleAxis=Component.UNDEFINED, withPolarRadiusAxis=Component.UNDEFINED, radarChartProps=Component.UNDEFINED, radarProps=Component.UNDEFINED, polarGridProps=Component.UNDEFINED, polarAngleAxisProps=Component.UNDEFINED, polarRadiusAxisProps=Component.UNDEFINED, clickData=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clickData', 'darkHidden', 'data', 'data-*', 'dataKey', 'display', 'ff', 'flex', 'fs', 'fw', 'fz', 'gridColor', 'h', 'hiddenFrom', 'inset', 'left', 'legendProps', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pe', 'pl', 'polarAngleAxisProps', 'polarGridProps', 'polarRadiusAxisProps', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radarChartProps', 'radarProps', 'right', 'series', 'style', 'styles', 'ta', 'tabIndex', 'td', 'textColor', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withLegend', 'withPolarAngleAxis', 'withPolarGrid', 'withPolarRadiusAxis']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clickData', 'darkHidden', 'data', 'data-*', 'dataKey', 'display', 'ff', 'flex', 'fs', 'fw', 'fz', 'gridColor', 'h', 'hiddenFrom', 'inset', 'left', 'legendProps', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pe', 'pl', 'polarAngleAxisProps', 'polarGridProps', 'polarRadiusAxisProps', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'radarChartProps', 'radarProps', 'right', 'series', 'style', 'styles', 'ta', 'tabIndex', 'td', 'textColor', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withLegend', 'withPolarAngleAxis', 'withPolarGrid', 'withPolarRadiusAxis']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['data', 'dataKey', 'series']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(RadarChart, self).__init__(children=children, **args)

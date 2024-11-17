# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AreaChart(Component):
    """An AreaChart component.
aChart

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Additional components that are rendered inside recharts
    `AreaChart` component.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- activeDotProps (dict; optional):
    Props passed down to all active dots. Ignored if
    `withDots={False}` is set.

- areaChartProps (dict; optional):
    Props passed down to recharts `AreaChart` component.

- areaProps (dict; optional):
    Props passed down to recharts `Area` component.

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

- clickSeriesName (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Name of the series that was clicked.

- connectNulls (boolean; optional):
    Determines whether points with `None` values should be connected,
    `True` by default.

- curveType (a value equal to: 'bump', 'linear', 'natural', 'monotone', 'step', 'stepBefore', 'stepAfter'; optional):
    Type of the curve, `'monotone'` by default.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data (list of dicts; required):
    Data used to display chart.

    `data` is a list of dicts with keys:


- data-* (string; optional):
    Wild card data attributes.

- dataKey (string; required):
    Key of the `data` object for x-axis values.

- display (boolean | number | string | dict | list; optional)

- dotProps (dict; optional):
    Props passed down to all dots. Ignored if `withDots={False}` is
    set.

- ff (boolean | number | string | dict | list; optional):
    FontFamily.

- fillOpacity (number; optional):
    Controls fill opacity of all areas, `0.2` by default.

- flex (string | number; optional)

- fs (boolean | number | string | dict | list; optional):
    FontStyle.

- fw (boolean | number | string | dict | list; optional):
    FontWeight.

- fz (number; optional):
    FontSize, theme key: theme.fontSizes.

- gridAxis (a value equal to: 'none', 'x', 'y', 'xy'; optional):
    Specifies which lines should be displayed in the grid, `'x'` by
    default.

- gridColor (boolean | number | string | dict | list; optional):
    Color of the grid and cursor lines, by default depends on color
    scheme.

- gridProps (dict; optional):
    Props passed down to the `CartesianGrid` component.

- h (string | number; optional):
    Height, theme key: theme.spacing.

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- highlightHover (boolean; default False):
    Determines whether a hovered series is highlighted. False by
    default. Mirrors the behaviour when hovering about chart legend
    items.

- hoverData (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Hover data.

- hoverSeriesName (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Name of the series that is hovered.

- inset (string | number; optional)

- left (string | number; optional)

- legendProps (dict; optional):
    Props passed down to the `Legend` component.

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

- orientation (a value equal to: 'horizontal', 'vertical'; optional):
    Chart orientation, `'horizontal'` by default.

- p (number; optional):
    Padding, theme key: theme.spacing.

- pb (number; optional):
    PaddingBottom, theme key: theme.spacing.

- pe (number; optional):
    PaddingInlineEnd, theme key: theme.spacing.

- pl (number; optional):
    PaddingLeft, theme key: theme.spacing.

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

- referenceLines (list of dicts; optional):
    Reference lines that should be displayed on the chart.

- right (string | number; optional)

- rightYAxisLabel (boolean | number | string | dict | list; optional):
    Props passed down to the YAxis recharts component rendered on the
    right side.

- rightYAxisProps (boolean | number | string | dict | list; optional):
    Props passed down to the YAxis recharts component rendered on the
    right side.

- series (list of dicts; required):
    An array of objects with `name` and `color` keys. Determines which
    data should be consumed from the `data` array.

    `series` is a list of dicts with keys:

    - strokeDasharray (string | number; optional)

    - color (boolean | number | string | dict | list; required)

    - name (string; required)

    - label (string; optional)

    - yAxisId (string; optional)

- splitColors (list of 2 elements: [boolean | number | string | dict | list, boolean | number | string | dict | list]; optional):
    A tuple of colors used when `type=\"split\"` is set, ignored in
    all other cases. A tuple may include theme colors reference or any
    valid CSS colors `['green.7', 'red.7']` by default.

- splitOffset (number; optional):
    Offset for the split gradient. By default, value is inferred from
    `data` and `series` if possible. Must be generated from the data
    array with `getSplitOffset` function.

- strokeDasharray (string | number; optional):
    Dash array for the grid lines and cursor, `'5 5'` by default.

- strokeWidth (number; optional):
    Stroke width for the chart areas, `2` by default.

- style (boolean | number | string | dict | list; optional):
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
    Color of the text displayed inside the chart, `'dimmed'` by
    default.

- tickLine (a value equal to: 'none', 'x', 'y', 'xy'; optional):
    Specifies which axis should have tick line, `'y'` by default.

- tooltipAnimationDuration (number; optional):
    Tooltip position animation duration in ms, `0` by default.

- tooltipProps (dict; optional):
    Props passed down to the `Tooltip` component.

- top (string | number; optional)

- tt (boolean | number | string | dict | list; optional):
    TextTransform.

- type (a value equal to: 'default', 'stacked', 'percent', 'split'; optional):
    Controls how chart areas are positioned relative to each other,
    `'default'` by default.

- unit (string; optional):
    Unit displayed next to each tick in y-axis.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional):
    Width, theme key: theme.spacing.

- withDots (boolean; optional):
    Determines whether dots should be displayed, `True` by default.

- withGradient (boolean; optional):
    Determines whether the chart area should be represented with a
    gradient instead of the solid color, `False` by default.

- withLegend (boolean; optional):
    Determines whether chart legend should be displayed, `False` by
    default.

- withPointLabels (boolean; optional):
    Determines whether each point should have associated label, False
    by default.

- withRightYAxis (boolean; optional):
    Determines whether additional y-axis should be displayed on the
    right side of the chart, False by default.

- withTooltip (boolean; optional):
    Determines whether chart tooltip should be displayed, `True` by
    default.

- withXAxis (boolean; optional):
    Determines whether x-axis should be hidden, `True` by default.

- withYAxis (boolean; optional):
    Determines whether y-axis should be hidden, `True` by default.

- xAxisLabel (string; optional):
    A label to display below the x-axis.

- xAxisProps (dict; optional):
    Props passed down to the `XAxis` recharts component.

- yAxisLabel (string; optional):
    A label to display next to the y-axis.

- yAxisProps (dict; optional):
    Props passed down to the `YAxis` recharts component."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'AreaChart'
    @_explicitize_args
    def __init__(self, children=None, data=Component.REQUIRED, series=Component.REQUIRED, type=Component.UNDEFINED, withGradient=Component.UNDEFINED, curveType=Component.UNDEFINED, withDots=Component.UNDEFINED, dotProps=Component.UNDEFINED, activeDotProps=Component.UNDEFINED, strokeWidth=Component.UNDEFINED, areaChartProps=Component.UNDEFINED, areaProps=Component.UNDEFINED, fillOpacity=Component.UNDEFINED, splitColors=Component.UNDEFINED, splitOffset=Component.UNDEFINED, connectNulls=Component.UNDEFINED, withPointLabels=Component.UNDEFINED, clickData=Component.UNDEFINED, hoverData=Component.UNDEFINED, clickSeriesName=Component.UNDEFINED, hoverSeriesName=Component.UNDEFINED, highlightHover=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, dataKey=Component.REQUIRED, referenceLines=Component.UNDEFINED, withXAxis=Component.UNDEFINED, withYAxis=Component.UNDEFINED, xAxisProps=Component.UNDEFINED, yAxisProps=Component.UNDEFINED, gridProps=Component.UNDEFINED, tickLine=Component.UNDEFINED, strokeDasharray=Component.UNDEFINED, gridAxis=Component.UNDEFINED, unit=Component.UNDEFINED, tooltipAnimationDuration=Component.UNDEFINED, legendProps=Component.UNDEFINED, tooltipProps=Component.UNDEFINED, withLegend=Component.UNDEFINED, withTooltip=Component.UNDEFINED, textColor=Component.UNDEFINED, gridColor=Component.UNDEFINED, orientation=Component.UNDEFINED, xAxisLabel=Component.UNDEFINED, yAxisLabel=Component.UNDEFINED, withRightYAxis=Component.UNDEFINED, rightYAxisProps=Component.UNDEFINED, rightYAxisLabel=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'activeDotProps', 'areaChartProps', 'areaProps', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clickData', 'clickSeriesName', 'connectNulls', 'curveType', 'darkHidden', 'data', 'data-*', 'dataKey', 'display', 'dotProps', 'ff', 'fillOpacity', 'flex', 'fs', 'fw', 'fz', 'gridAxis', 'gridColor', 'gridProps', 'h', 'hiddenFrom', 'highlightHover', 'hoverData', 'hoverSeriesName', 'inset', 'left', 'legendProps', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'orientation', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'referenceLines', 'right', 'rightYAxisLabel', 'rightYAxisProps', 'series', 'splitColors', 'splitOffset', 'strokeDasharray', 'strokeWidth', 'style', 'styles', 'ta', 'tabIndex', 'td', 'textColor', 'tickLine', 'tooltipAnimationDuration', 'tooltipProps', 'top', 'tt', 'type', 'unit', 'unstyled', 'variant', 'visibleFrom', 'w', 'withDots', 'withGradient', 'withLegend', 'withPointLabels', 'withRightYAxis', 'withTooltip', 'withXAxis', 'withYAxis', 'xAxisLabel', 'xAxisProps', 'yAxisLabel', 'yAxisProps']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'activeDotProps', 'areaChartProps', 'areaProps', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clickData', 'clickSeriesName', 'connectNulls', 'curveType', 'darkHidden', 'data', 'data-*', 'dataKey', 'display', 'dotProps', 'ff', 'fillOpacity', 'flex', 'fs', 'fw', 'fz', 'gridAxis', 'gridColor', 'gridProps', 'h', 'hiddenFrom', 'highlightHover', 'hoverData', 'hoverSeriesName', 'inset', 'left', 'legendProps', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'orientation', 'p', 'pb', 'pe', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'referenceLines', 'right', 'rightYAxisLabel', 'rightYAxisProps', 'series', 'splitColors', 'splitOffset', 'strokeDasharray', 'strokeWidth', 'style', 'styles', 'ta', 'tabIndex', 'td', 'textColor', 'tickLine', 'tooltipAnimationDuration', 'tooltipProps', 'top', 'tt', 'type', 'unit', 'unstyled', 'variant', 'visibleFrom', 'w', 'withDots', 'withGradient', 'withLegend', 'withPointLabels', 'withRightYAxis', 'withTooltip', 'withXAxis', 'withYAxis', 'xAxisLabel', 'xAxisProps', 'yAxisLabel', 'yAxisProps']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['data', 'dataKey', 'series']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AreaChart, self).__init__(children=children, **args)

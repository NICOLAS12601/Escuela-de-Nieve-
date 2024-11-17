# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DonutChart(Component):
    """A DonutChart component.
utChart

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Additional elements rendered inside `PieChart` component.

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

- chartLabel (string | number; optional):
    Chart label, displayed in the center of the chart.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- clickData (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Click data.

- clickSeriesName (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Name of the series that was clicked.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data (list of dicts; required):
    Data used to render chart.

    `data` is a list of dicts with keys:

    - name (string; required)

    - value (number; required)

    - color (boolean | number | string | dict | list; required)

- data-* (string; optional):
    Wild card data attributes.

- display (boolean | number | string | dict | list; optional)

- endAngle (number; optional):
    Controls angle at which charts ends, `360` by default. Set to `0`
    to render the chart as semicircle.

- ff (boolean | number | string | dict | list; optional):
    FontFamily.

- flex (string | number; optional)

- fs (boolean | number | string | dict | list; optional):
    FontStyle.

- fw (boolean | number | string | dict | list; optional):
    FontWeight.

- fz (number; optional):
    FontSize, theme key: theme.fontSizes.

- h (string | number; optional):
    Height, theme key: theme.spacing.

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- hoverData (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Hover data.

- hoverSeriesName (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Name of the series that is hovered.

- inset (string | number; optional)

- labelColor (boolean | number | string | dict | list; optional):
    Controls text color of all labels, by default depends on color
    scheme.

- left (string | number; optional)

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

- paddingAngle (number; optional):
    Controls padding between segments, `0` by default.

- pb (number; optional):
    PaddingBottom, theme key: theme.spacing.

- pe (number; optional):
    PaddingInlineEnd, theme key: theme.spacing.

- pieChartProps (dict; optional):
    Props passed down to recharts `PieChart` component.

- pieProps (boolean | number | string | dict | list; optional):
    Props passed down to recharts `Pie` component.

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

- right (string | number; optional)

- size (number; optional):
    Controls chart width and height, height is increased by 40 if
    `withLabels` prop is set. Cannot be less than `thickness`. `80` by
    default.

- startAngle (number; optional):
    Controls angle at which chart starts, `0` by default. Set to `180`
    to render the chart as semicircle.

- strokeColor (boolean | number | string | dict | list; optional):
    Controls color of the segments stroke, by default depends on color
    scheme.

- strokeWidth (number; optional):
    Controls width of segments stroke, `1` by default.

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

- thickness (number; optional):
    Controls thickness of the chart segments, `20` by default.

- tooltipAnimationDuration (number; optional):
    Tooltip animation duration in ms, `0` by default.

- tooltipDataSource (a value equal to: 'segment', 'all'; optional):
    Determines which data is displayed in the tooltip. `'all'` –
    display all values, `'segment'` – display only hovered segment.
    `'all'` by default.

- tooltipProps (boolean | number | string | dict | list; optional):
    Props passed down to `Tooltip` recharts component.

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

- withLabels (boolean; optional):
    Determines whether each segment should have associated label,
    `False` by default.

- withLabelsLine (boolean; optional):
    Determines whether segments labels should have lines that connect
    the segment with the label, `True` by default.

- withTooltip (boolean; optional):
    Determines whether the tooltip should be displayed when one of the
    section is hovered, `True` by default."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'DonutChart'
    @_explicitize_args
    def __init__(self, children=None, data=Component.REQUIRED, withTooltip=Component.UNDEFINED, tooltipAnimationDuration=Component.UNDEFINED, tooltipProps=Component.UNDEFINED, pieProps=Component.UNDEFINED, strokeColor=Component.UNDEFINED, labelColor=Component.UNDEFINED, paddingAngle=Component.UNDEFINED, withLabels=Component.UNDEFINED, withLabelsLine=Component.UNDEFINED, thickness=Component.UNDEFINED, size=Component.UNDEFINED, strokeWidth=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, tooltipDataSource=Component.UNDEFINED, chartLabel=Component.UNDEFINED, pieChartProps=Component.UNDEFINED, clickData=Component.UNDEFINED, hoverData=Component.UNDEFINED, clickSeriesName=Component.UNDEFINED, hoverSeriesName=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'chartLabel', 'className', 'classNames', 'clickData', 'clickSeriesName', 'darkHidden', 'data', 'data-*', 'display', 'endAngle', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'hoverData', 'hoverSeriesName', 'inset', 'labelColor', 'left', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'p', 'paddingAngle', 'pb', 'pe', 'pieChartProps', 'pieProps', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'right', 'size', 'startAngle', 'strokeColor', 'strokeWidth', 'style', 'styles', 'ta', 'tabIndex', 'td', 'thickness', 'tooltipAnimationDuration', 'tooltipDataSource', 'tooltipProps', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withLabels', 'withLabelsLine', 'withTooltip']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'chartLabel', 'className', 'classNames', 'clickData', 'clickSeriesName', 'darkHidden', 'data', 'data-*', 'display', 'endAngle', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'hoverData', 'hoverSeriesName', 'inset', 'labelColor', 'left', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'opacity', 'p', 'paddingAngle', 'pb', 'pe', 'pieChartProps', 'pieProps', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'right', 'size', 'startAngle', 'strokeColor', 'strokeWidth', 'style', 'styles', 'ta', 'tabIndex', 'td', 'thickness', 'tooltipAnimationDuration', 'tooltipDataSource', 'tooltipProps', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withLabels', 'withLabelsLine', 'withTooltip']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DonutChart, self).__init__(children=children, **args)

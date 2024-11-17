# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class YearPicker(Component):
    """A YearPicker component.
ePicker

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- allowDeselect (boolean; optional):
    Determines whether user can deselect the date by clicking on
    selected item, applicable only when type=\"default\".

- allowSingleDateInRange (boolean; optional):
    Determines whether single year can be selected as range,
    applicable only when type=\"range\".

- aria-* (string; optional):
    Wild card aria attributes.

- ariaLabels (dict; optional):
    aria-label attributes for controls on different levels.

    `ariaLabels` is a dict with keys:

    - monthLevelControl (string; optional)

    - nextDecade (string; optional)

    - nextMonth (string; optional)

    - nextYear (string; optional)

    - previousDecade (string; optional)

    - previousMonth (string; optional)

    - previousYear (string; optional)

    - yearLevelControl (string; optional)

- bd (string | number; optional):
    border.

- bg (boolean | number | string | dict | list; optional):
    background, theme key: theme.colors.

- bga (boolean | number | string | dict | list; optional):
    backgroundAttachment.

- bgp (string | number; optional):
    backgroundPosition.

- bgr (boolean | number | string | dict | list; optional):
    backgroundRepeat.

- bgsz (string | number; optional):
    backgroundSize.

- bottom (string | number; optional)

- c (boolean | number | string | dict | list; optional):
    color.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- clearButtonProps (dict; optional):
    Props passed down to clear button.

- clearable (boolean; optional):
    Determines whether input value can be cleared, adds clear button
    to right section, False by default.

- closeOnChange (boolean; optional):
    Determines whether dropdown should be closed when date is
    selected, not applicable when type=\"multiple\", True by default.

- columnsToScroll (number; optional):
    Number of columns to scroll when user clicks next/prev buttons,
    defaults to numberOfColumns.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- debounce (number; default 0):
    Debounce time in ms.

- decadeLabelFormat (string; optional):
    dayjs label format to display decade label or a function that
    returns decade label based on date value, defaults to \"YYYY\".

- description (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Description` component. If not set, description
    is not rendered.

- descriptionProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Description` component.

- disabled (boolean; optional):
    Sets `disabled` attribute on the `input` element.

- disabledDates (list of strings; optional):
    Specifies days that should be disabled.

- display (boolean | number | string | dict | list; optional)

- dropdownType (a value equal to: 'popover', 'modal'; optional):
    Type of dropdown, defaults to popover.

- error (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Error` component. If not set, error is not
    rendered.

- errorProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Error` component.

- ff (boolean | number | string | dict | list; optional):
    fontFamily.

- firstDayOfWeek (a value equal to: 0, 1, 2, 3, 4, 5, 6; optional):
    number 0-6, 0 – Sunday, 6 – Saturday, defaults to 1 – Monday.

- flex (string | number; optional)

- fs (boolean | number | string | dict | list; optional):
    fontStyle.

- fw (boolean | number | string | dict | list; optional):
    fontWeight.

- fz (number; optional):
    fontSize, theme key: theme.fontSizes.

- h (string | number; optional):
    height, theme key: theme.spacing.

- hasNextLevel (boolean; optional):
    Determines whether next level button should be enabled, defaults
    to True.

- hiddenFrom (boolean | number | string | dict | list; optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- hideOutsideDates (boolean; optional):
    Determines whether outside dates should be hidden, defaults to
    False.

- hideWeekdays (boolean; optional):
    Determines whether weekdays row should be hidden, defaults to
    False.

- inputWrapperOrder (list of a value equal to: 'label', 'description', 'error', 'input's; optional):
    Controls order of the elements, `['label', 'description', 'input',
    'error']` by default.

- inset (string | number; optional)

- label (a list of or a singular dash component, string or number; optional):
    Contents of `Input.Label` component. If not set, label is not
    rendered.

- labelProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the `Input.Label` component.

- labelSeparator (string; optional):
    Separator between range value.

- left (string | number; optional)

- leftSection (a list of or a singular dash component, string or number; optional):
    Content section rendered on the left side of the input.

- leftSectionPointerEvents (a value equal to: '-moz-initial', 'inherit', 'initial', 'revert', 'revert-layer', 'unset', 'auto', 'none', 'all', 'fill', 'painted', 'stroke', 'visible', 'visibleFill', 'visiblePainted', 'visibleStroke'; optional):
    Sets `pointer-events` styles on the `leftSection` element,
    `'none'` by default.

- leftSectionProps (dict; optional):
    Props passed down to the `leftSection` element.

- leftSectionWidth (string | number; optional):
    Left section width, used to set `width` of the section and input
    `padding-left`, by default equals to the input height.

- level (a value equal to: 'month', 'year', 'decade'; optional):
    Current level displayed to the user (decade, year, month), used
    for controlled component.

- lh (number; optional):
    lineHeight, theme key: lineHeights.

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

- lts (string | number; optional):
    letterSpacing.

- m (number; optional):
    margin, theme key: theme.spacing.

- mah (string | number; optional):
    maxHeight, theme key: theme.spacing.

- maw (string | number; optional):
    maxWidth, theme key: theme.spacing.

- maxDate (string; optional):
    Maximum possible date.

- mb (number; optional):
    marginBottom, theme key: theme.spacing.

- me (number; optional):
    marginInlineEnd, theme key: theme.spacing.

- mih (string | number; optional):
    minHeight, theme key: theme.spacing.

- minDate (string; optional):
    Minimum possible date.

- miw (string | number; optional):
    minWidth, theme key: theme.spacing.

- ml (number; optional):
    marginLeft, theme key: theme.spacing.

- mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Element modifiers transformed into `data-` attributes, for
    example, `{ 'data-size': 'xl' }`, falsy values are removed.

- modalProps (dict; optional):
    Props passed down to Modal component.

    `modalProps` is a dict with keys:

    - bd (string | number; optional):
        border.

    - bg (boolean | number | string | dict | list; optional):
        background, theme key: theme.colors.

    - bga (boolean | number | string | dict | list; optional):
        backgroundAttachment.

    - bgp (string | number; optional):
        backgroundPosition.

    - bgr (boolean | number | string | dict | list; optional):
        backgroundRepeat.

    - bgsz (string | number; optional):
        backgroundSize.

    - bottom (string | number; optional)

    - c (boolean | number | string | dict | list; optional):
        color.

    - centered (boolean; optional):
        Determines whether the modal should be centered vertically,
        `False` by default.

    - className (string; optional):
        Class added to the root element, if applicable.

    - closeButtonProps (dict; optional):
        Props passed down to the close button.

        `closeButtonProps` is a dict with keys:

        - bd (string | number; optional):
            border.

        - bg (boolean | number | string | dict | list; optional):
            background, theme key: theme.colors.

        - bga (boolean | number | string | dict | list; optional):
            backgroundAttachment.

        - bgp (string | number; optional):
            backgroundPosition.

        - bgr (boolean | number | string | dict | list; optional):
            backgroundRepeat.

        - bgsz (string | number; optional):
            backgroundSize.

        - bottom (string | number; optional)

        - c (boolean | number | string | dict | list; optional):
            color.

        - children (a list of or a singular dash component, string or number; optional):
            Content rendered inside the button, for example
            `VisuallyHidden` with label for screen readers.

        - className (string; optional):
            Class added to the root element, if applicable.

        - darkHidden (boolean; optional):
            Determines whether component should be hidden in dark
            color scheme with `display: none`.

        - disabled (boolean; optional):
            Sets `disabled` and `data-disabled` attributes on the
            button element.

        - display (boolean | number | string | dict | list; optional)

        - ff (boolean | number | string | dict | list; optional):
            fontFamily.

        - flex (string | number; optional)

        - fs (boolean | number | string | dict | list; optional):
            fontStyle.

        - fw (boolean | number | string | dict | list; optional):
            fontWeight.

        - fz (number; optional):
            fontSize, theme key: theme.fontSizes.

        - h (string | number; optional):
            height, theme key: theme.spacing.

        - hiddenFrom (boolean | number | string | dict | list; optional):
            Breakpoint above which the component is hidden with
            `display: none`.

        - icon (a list of or a singular dash component, string or number; optional):
            Replaces default close icon. If set, `iconSize` prop is
            ignored.

        - iconSize (string | number; optional):
            `X` icon `width` and `height`, `80%` by default.

        - inset (string | number; optional)

        - left (string | number; optional)

        - lh (number; optional):
            lineHeight, theme key: lineHeights.

        - lightHidden (boolean; optional):
            Determines whether component should be hidden in light
            color scheme with `display: none`.

        - lts (string | number; optional):
            letterSpacing.

        - m (number; optional):
            margin, theme key: theme.spacing.

        - mah (string | number; optional):
            maxHeight, theme key: theme.spacing.

        - maw (string | number; optional):
            maxWidth, theme key: theme.spacing.

        - mb (number; optional):
            marginBottom, theme key: theme.spacing.

        - me (number; optional):
            marginInlineEnd, theme key: theme.spacing.

        - mih (string | number; optional):
            minHeight, theme key: theme.spacing.

        - miw (string | number; optional):
            minWidth, theme key: theme.spacing.

        - ml (number; optional):
            marginLeft, theme key: theme.spacing.

        - mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
            Element modifiers transformed into `data-` attributes, for
            example, `{ 'data-size': 'xl' }`, falsy values are
            removed.

        - mr (number; optional):
            marginRight, theme key: theme.spacing.

        - ms (number; optional):
            marginInlineStart, theme key: theme.spacing.

        - mt (number; optional):
            marginTop, theme key: theme.spacing.

        - mx (number; optional):
            marginInline, theme key: theme.spacing.

        - my (number; optional):
            marginBlock, theme key: theme.spacing.

        - opacity (boolean | number | string | dict | list; optional)

        - p (number; optional):
            padding, theme key: theme.spacing.

        - pb (number; optional):
            paddingBottom, theme key: theme.spacing.

        - pe (number; optional):
            paddingInlineEnd, theme key: theme.spacing.

        - pl (number; optional):
            paddingLeft, theme key: theme.spacing.

        - pos (boolean | number | string | dict | list; optional):
            position.

        - pr (number; optional):
            paddingRight, theme key: theme.spacing.

        - ps (number; optional):
            paddingInlineStart, theme key: theme.spacing.

        - pt (number; optional):
            paddingTop, theme key: theme.spacing.

        - px (number; optional):
            paddingInline, theme key: theme.spacing.

        - py (number; optional):
            paddingBlock, theme key: theme.spacing.

        - radius (number; optional):
            Key of `theme.radius` or any valid CSS value to set
            border-radius. Numbers are converted to rem.
            `theme.defaultRadius` by default.

        - right (string | number; optional)

        - size (number; optional):
            Controls width and height of the button. Numbers are
            converted to rem. `'md'` by default.

        - style (optional):
            Inline style added to root component element, can
            subscribe to theme defined on MantineProvider.

        - ta (boolean | number | string | dict | list; optional):
            textAlign.

        - td (string | number; optional):
            textDecoration.

        - top (string | number; optional)

        - tt (boolean | number | string | dict | list; optional):
            textTransform.

        - visibleFrom (boolean | number | string | dict | list; optional):
            Breakpoint below which the component is hidden with
            `display: none`.

        - w (string | number; optional):
            width, theme key: theme.spacing.

    - closeOnClickOutside (boolean; optional):
        Determines whether the modal/drawer should be closed when user
        clicks on the overlay, `True` by default.

    - closeOnEscape (boolean; optional):
        Determines whether `onClose` should be called when user
        presses the escape key, `True` by default.

    - darkHidden (boolean; optional):
        Determines whether component should be hidden in dark color
        scheme with `display: none`.

    - display (boolean | number | string | dict | list; optional)

    - ff (boolean | number | string | dict | list; optional):
        fontFamily.

    - flex (string | number; optional)

    - fs (boolean | number | string | dict | list; optional):
        fontStyle.

    - fullScreen (boolean; optional):
        Determines whether the modal should take the entire screen,
        `False` by default.

    - fw (boolean | number | string | dict | list; optional):
        fontWeight.

    - fz (number; optional):
        fontSize, theme key: theme.fontSizes.

    - h (string | number; optional):
        height, theme key: theme.spacing.

    - hiddenFrom (boolean | number | string | dict | list; optional):
        Breakpoint above which the component is hidden with `display:
        none`.

    - inset (string | number; optional)

    - keepMounted (boolean; optional):
        If set modal/drawer will not be unmounted from the DOM when it
        is hidden, `display: none` styles will be added instead,
        `False` by default.

    - left (string | number; optional)

    - lh (number; optional):
        lineHeight, theme key: lineHeights.

    - lightHidden (boolean; optional):
        Determines whether component should be hidden in light color
        scheme with `display: none`.

    - lockScroll (boolean; optional):
        Determines whether scroll should be locked when
        `opened={True}`, `True` by default.

    - lts (string | number; optional):
        letterSpacing.

    - m (number; optional):
        margin, theme key: theme.spacing.

    - mah (string | number; optional):
        maxHeight, theme key: theme.spacing.

    - maw (string | number; optional):
        maxWidth, theme key: theme.spacing.

    - mb (number; optional):
        marginBottom, theme key: theme.spacing.

    - me (number; optional):
        marginInlineEnd, theme key: theme.spacing.

    - mih (string | number; optional):
        minHeight, theme key: theme.spacing.

    - miw (string | number; optional):
        minWidth, theme key: theme.spacing.

    - ml (number; optional):
        marginLeft, theme key: theme.spacing.

    - mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
        Element modifiers transformed into `data-` attributes, for
        example, `{ 'data-size': 'xl' }`, falsy values are removed.

    - mr (number; optional):
        marginRight, theme key: theme.spacing.

    - ms (number; optional):
        marginInlineStart, theme key: theme.spacing.

    - mt (number; optional):
        marginTop, theme key: theme.spacing.

    - mx (number; optional):
        marginInline, theme key: theme.spacing.

    - my (number; optional):
        marginBlock, theme key: theme.spacing.

    - opacity (boolean | number | string | dict | list; optional)

    - opened (boolean; optional):
        Determines whether modal/drawer is opened.

    - overlayProps (dict; optional):
        Props passed down to the `Overlay` component, use to configure
        opacity, `background-color`, styles and other properties.

        `overlayProps` is a dict with keys:

        - backgroundOpacity (number; optional):
            Controls overlay `background-color` opacity 0–1,
            disregarded when `gradient` prop is set, `0.6` by default.

        - bd (string | number; optional):
            border.

        - bg (boolean | number | string | dict | list; optional):
            background, theme key: theme.colors.

        - bga (boolean | number | string | dict | list; optional):
            backgroundAttachment.

        - bgp (string | number; optional):
            backgroundPosition.

        - bgr (boolean | number | string | dict | list; optional):
            backgroundRepeat.

        - bgsz (string | number; optional):
            backgroundSize.

        - blur (string | number; optional):
            Overlay background blur, `0` by default.

        - bottom (string | number; optional)

        - c (boolean | number | string | dict | list; optional):
            color.

        - center (boolean; optional):
            Determines whether content inside overlay should be
            vertically and horizontally centered, `False` by default.

        - children (a list of or a singular dash component, string or number; optional):
            Content inside overlay.

        - className (string; optional):
            Class added to the root element, if applicable.

        - color (boolean | number | string | dict | list; optional):
            Overlay `background-color`, `#000` by default.

        - darkHidden (boolean; optional):
            Determines whether component should be hidden in dark
            color scheme with `display: none`.

        - display (boolean | number | string | dict | list; optional)

        - ff (boolean | number | string | dict | list; optional):
            fontFamily.

        - fixed (boolean; optional):
            Determines whether overlay should have fixed position
            instead of absolute, `False` by default.

        - flex (string | number; optional)

        - fs (boolean | number | string | dict | list; optional):
            fontStyle.

        - fw (boolean | number | string | dict | list; optional):
            fontWeight.

        - fz (number; optional):
            fontSize, theme key: theme.fontSizes.

        - gradient (string; optional):
            Changes overlay to gradient. If set, `color` prop is
            ignored.

        - h (string | number; optional):
            height, theme key: theme.spacing.

        - hiddenFrom (boolean | number | string | dict | list; optional):
            Breakpoint above which the component is hidden with
            `display: none`.

        - inset (string | number; optional)

        - left (string | number; optional)

        - lh (number; optional):
            lineHeight, theme key: lineHeights.

        - lightHidden (boolean; optional):
            Determines whether component should be hidden in light
            color scheme with `display: none`.

        - lts (string | number; optional):
            letterSpacing.

        - m (number; optional):
            margin, theme key: theme.spacing.

        - mah (string | number; optional):
            maxHeight, theme key: theme.spacing.

        - maw (string | number; optional):
            maxWidth, theme key: theme.spacing.

        - mb (number; optional):
            marginBottom, theme key: theme.spacing.

        - me (number; optional):
            marginInlineEnd, theme key: theme.spacing.

        - mih (string | number; optional):
            minHeight, theme key: theme.spacing.

        - miw (string | number; optional):
            minWidth, theme key: theme.spacing.

        - ml (number; optional):
            marginLeft, theme key: theme.spacing.

        - mod (string | dict with strings as keys and values of type boolean | number | string | dict | list; optional):
            Element modifiers transformed into `data-` attributes, for
            example, `{ 'data-size': 'xl' }`, falsy values are
            removed.

        - mr (number; optional):
            marginRight, theme key: theme.spacing.

        - ms (number; optional):
            marginInlineStart, theme key: theme.spacing.

        - mt (number; optional):
            marginTop, theme key: theme.spacing.

        - mx (number; optional):
            marginInline, theme key: theme.spacing.

        - my (number; optional):
            marginBlock, theme key: theme.spacing.

        - opacity (boolean | number | string | dict | list; optional)

        - p (number; optional):
            padding, theme key: theme.spacing.

        - pb (number; optional):
            paddingBottom, theme key: theme.spacing.

        - pe (number; optional):
            paddingInlineEnd, theme key: theme.spacing.

        - pl (number; optional):
            paddingLeft, theme key: theme.spacing.

        - pos (boolean | number | string | dict | list; optional):
            position.

        - pr (number; optional):
            paddingRight, theme key: theme.spacing.

        - ps (number; optional):
            paddingInlineStart, theme key: theme.spacing.

        - pt (number; optional):
            paddingTop, theme key: theme.spacing.

        - px (number; optional):
            paddingInline, theme key: theme.spacing.

        - py (number; optional):
            paddingBlock, theme key: theme.spacing.

        - radius (number; optional):
            Key of `theme.radius` or any valid CSS value to set
            border-radius, `0` by default.

        - right (string | number; optional)

        - style (optional):
            Inline style added to root component element, can
            subscribe to theme defined on MantineProvider.

        - ta (boolean | number | string | dict | list; optional):
            textAlign.

        - td (string | number; optional):
            textDecoration.

        - top (string | number; optional)

        - transitionProps (dict; optional):
            Props passed down to the `Transition` component.

            `transitionProps` is a dict with keys:

            - duration (number; optional):
                Transition duration in ms, `250` by default.

            - exitDuration (number; optional):
                Exit transition duration in ms, `250` by default.

            - keepMounted (boolean; optional):
                If set element will not be unmounted from the DOM when
                it is hidden, `display: none` styles will be applied
                instead.

            - mounted (boolean; required):
                Determines whether component should be mounted to the
                DOM.

            - timingFunction (string; optional):
                Transition timing function,
                `theme.transitionTimingFunction` by default.

            - transition (boolean | number | string | dict | list; optional):
                Transition name or object.

        - tt (boolean | number | string | dict | list; optional):
            textTransform.

        - unstyled (boolean; optional):
            Remove all Mantine styling from the component.

        - visibleFrom (boolean | number | string | dict | list; optional):
            Breakpoint below which the component is hidden with
            `display: none`.

        - w (string | number; optional):
            width, theme key: theme.spacing.

        - zIndex (string | number; optional):
            Overlay z-index, `200` by default.

    - p (number; optional):
        padding, theme key: theme.spacing.

    - padding (number; optional):
        Key of `theme.spacing` or any valid CSS value to set content,
        header and footer padding, `'md'` by default.

    - pb (number; optional):
        paddingBottom, theme key: theme.spacing.

    - pe (number; optional):
        paddingInlineEnd, theme key: theme.spacing.

    - pl (number; optional):
        paddingLeft, theme key: theme.spacing.

    - portalProps (dict; optional):
        Props passed down to the Portal component when `withinPortal`
        is set.

    - pos (boolean | number | string | dict | list; optional):
        position.

    - pr (number; optional):
        paddingRight, theme key: theme.spacing.

    - ps (number; optional):
        paddingInlineStart, theme key: theme.spacing.

    - pt (number; optional):
        paddingTop, theme key: theme.spacing.

    - px (number; optional):
        paddingInline, theme key: theme.spacing.

    - py (number; optional):
        paddingBlock, theme key: theme.spacing.

    - radius (number; optional):
        Key of `theme.radius` or any valid CSS value to set
        `border-radius`, `theme.defaultRadius` by default.

    - removeScrollProps (dict; optional):
        Props passed down to react-remove-scroll, can be used to
        customize scroll lock behavior.

    - returnFocus (boolean; optional):
        Determines whether focus should be returned to the last active
        element when `onClose` is called, `True` by default.

    - right (string | number; optional)

    - shadow (boolean | number | string | dict | list; optional):
        Key of `theme.shadows` or any valid CSS box-shadow value, 'xl'
        by default.

    - size (number; optional):
        Controls width of the content area, `'md'` by default.

    - style (optional):
        Inline style added to root component element, can subscribe to
        theme defined on MantineProvider.

    - ta (boolean | number | string | dict | list; optional):
        textAlign.

    - td (string | number; optional):
        textDecoration.

    - title (a list of or a singular dash component, string or number; optional):
        Modal title.

    - top (string | number; optional)

    - transitionProps (dict; optional):
        Props added to the `Transition` component that used to animate
        overlay and body, use to configure duration and animation
        type, `{ duration: 200, transition: 'pop' }` by default.

        `transitionProps` is a dict with keys:

        - duration (number; optional):
            Transition duration in ms, `250` by default.

        - exitDuration (number; optional):
            Exit transition duration in ms, `250` by default.

        - keepMounted (boolean; optional):
            If set element will not be unmounted from the DOM when it
            is hidden, `display: none` styles will be applied instead.

        - mounted (boolean; required):
            Determines whether component should be mounted to the DOM.

        - timingFunction (string; optional):
            Transition timing function,
            `theme.transitionTimingFunction` by default.

        - transition (boolean | number | string | dict | list; optional):
            Transition name or object.

    - trapFocus (boolean; optional):
        Determines whether focus should be trapped, `True` by default.

    - tt (boolean | number | string | dict | list; optional):
        textTransform.

    - visibleFrom (boolean | number | string | dict | list; optional):
        Breakpoint below which the component is hidden with `display:
        none`.

    - w (string | number; optional):
        width, theme key: theme.spacing.

    - withCloseButton (boolean; optional):
        Determines whether the close button should be rendered, `True`
        by default.

    - withOverlay (boolean; optional):
        Determines whether the overlay should be rendered, `True` by
        default.

    - withinPortal (boolean; optional):
        Determines whether the component should be rendered inside
        `Portal`, `True` by default.

    - xOffset (string | number; optional):
        Left/right modal offset, `5vw` by default.

    - yOffset (string | number; optional):
        Top/bottom modal offset, `5dvh` by default.

    - zIndex (string | number; optional):
        `z-index` CSS property of the root element, `200` by default.

- monthLabelFormat (string; optional):
    dayjs label format to display month label or a function that
    returns month label based on month value, defaults to \"MMMM
    YYYY\".

- monthsListFormat (string; optional):
    dayjs format for months list.

- mr (number; optional):
    marginRight, theme key: theme.spacing.

- ms (number; optional):
    marginInlineStart, theme key: theme.spacing.

- mt (number; optional):
    marginTop, theme key: theme.spacing.

- mx (number; optional):
    marginInline, theme key: theme.spacing.

- my (number; optional):
    marginBlock, theme key: theme.spacing.

- n_submit (number; default 0):
    An integer that represents the number of times that this element
    has been submitted.

- name (string; optional):
    Name prop.

- nextIcon (a list of or a singular dash component, string or number; optional):
    Change next icon.

- nextLabel (string; optional):
    aria-label for next button.

- numberOfColumns (number; optional):
    Number of columns to render next to each other.

- opacity (boolean | number | string | dict | list; optional)

- p (number; optional):
    padding, theme key: theme.spacing.

- pb (number; optional):
    paddingBottom, theme key: theme.spacing.

- pe (number; optional):
    paddingInlineEnd, theme key: theme.spacing.

- persisted_props (list of strings; default ["value"]):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- pl (number; optional):
    paddingLeft, theme key: theme.spacing.

- placeholder (string; optional):
    Input placeholder.

- pointer (boolean; optional):
    Determines whether the input should have `cursor: pointer` style,
    `False` by default.

- popoverProps (dict; optional):
    Props passed down to Popover component.

    `popoverProps` is a dict with keys:

    - arrowOffset (number; optional):
        Arrow offset in px, `5` by default.

    - arrowPosition (a value equal to: 'center', 'side'; optional):
        Arrow position.

    - arrowRadius (number; optional):
        Arrow `border-radius` in px, `0` by default.

    - arrowSize (number; optional):
        Arrow size in px, `7` by default.

    - classNames (dict; optional):
        Adds class names to Mantine components.

    - clickOutsideEvents (list of strings; optional):
        Events that trigger outside clicks.

    - closeOnClickOutside (boolean; optional):
        Determines whether dropdown should be closed on outside
        clicks, `True` by default.

    - closeOnEscape (boolean; optional):
        Determines whether dropdown should be closed when `Escape` key
        is pressed, `True` by default.

    - disabled (boolean; optional):
        If set, popover dropdown will not be rendered.

    - floatingStrategy (a value equal to: 'absolute', 'fixed'; optional):
        Changes floating ui [position
        strategy](https://floating-ui.com/docs/usefloating#strategy),
        `'absolute'` by default.

    - keepMounted (boolean; optional):
        If set dropdown will not be unmounted from the DOM when it is
        hidden, `display: none` styles will be added instead.

    - middlewares (dict; optional):
        Floating ui middlewares to configure position handling, `{
        flip: True, shift: True, inline: False }` by default.

        `middlewares` is a dict with keys:

        - flip (dict; optional)

            `flip` is a dict with keys:

    - altBoundary (boolean; optional):
        Whether to check for overflow using the alternate element's
        boundary  (`clippingAncestors` boundary only).
        @,default,False.

    - boundary (dict; optional)

        `boundary` is a dict with keys:

        - height (number; required)

        - width (number; required)

        - x (number; required)

        - y (number; required)

              Or list of a list of or a singular dash component, string or numbers

    - crossAxis (boolean; optional):
        The axis that runs along the alignment of the floating
        element. Determines  whether overflow along this axis is
        checked to perform a flip. @,default,True.

    - elementContext (a value equal to: 'reference', 'floating'; optional):
        The element in which overflow is being checked relative to a
        boundary. @,default,'floating'.

    - fallbackAxisSideDirection (a value equal to: 'end', 'start', 'none'; optional):
        Whether to allow fallback to the perpendicular axis of the
        preferred  placement, and if so, which side direction along
        the axis to prefer. @,default,'none' (disallow fallback).

    - fallbackPlacements (list of a value equal to: 'top', 'left', 'bottom', 'right', 'top-end', 'top-start', 'left-end', 'left-start', 'bottom-end', 'bottom-start', 'right-end', 'right-start's; optional):
        Placements to try sequentially if the preferred `placement`
        does not fit. @,default,[oppositePlacement] (computed).

    - fallbackStrategy (a value equal to: 'bestFit', 'initialPlacement'; optional):
        What strategy to use when no placements fit.
        @,default,'bestFit'.

    - flipAlignment (boolean; optional):
        Whether to flip to placements with the opposite alignment if
        they fit  better. @,default,True.

    - mainAxis (boolean; optional):
        The axis that runs along the side of the floating element.
        Determines  whether overflow along this axis is checked to
        perform a flip. @,default,True.

    - padding (dict; optional):
        Virtual padding for the resolved overflow detection offsets.
        @,default,0.

        `padding` is a number

          Or dict with keys:

        - bottom (number; optional)

        - left (number; optional)

        - right (number; optional)

        - top (number; optional)

    - rootBoundary (dict; optional):
        The root clipping area in which overflow will be checked.
        @,default,'viewport'.

        `rootBoundary` is a dict with keys:

        - height (number; required)

        - width (number; required)

        - x (number; required)

        - y (number; required)

        - inline (boolean | number | string | dict | list; optional)

        - shift (optional)

        - size (optional)

    - offset (number; optional):
        Offset of the dropdown element, `8` by default.

    - opened (boolean; optional):
        Controlled dropdown opened state.

    - portalProps (dict; optional):
        Props to pass down to the `Portal` when `withinPortal` is
        True.

    - position (a value equal to: 'top', 'left', 'bottom', 'right', 'top-end', 'top-start', 'left-end', 'left-start', 'bottom-end', 'bottom-start', 'right-end', 'right-start'; optional):
        Dropdown position relative to the target element, `'bottom'`
        by default.

    - positionDependencies (list of boolean | number | string | dict | lists; optional):
        `useEffect` dependencies to force update dropdown position,
        `[]` by default.

    - radius (number; optional):
        Key of `theme.radius` or any valid CSS value to set
        border-radius, `theme.defaultRadius` by default.

    - returnFocus (boolean; optional):
        Determines whether focus should be automatically returned to
        control when dropdown closes, `False` by default.

    - shadow (boolean | number | string | dict | list; optional):
        Key of `theme.shadows` or any other valid CSS `box-shadow`
        value.

    - styles (boolean | number | string | dict | list; optional):
        Mantine styles API.

    - transitionProps (dict; optional):
        Props passed down to the `Transition` component that used to
        animate dropdown presence, use to configure duration and
        animation type, `{ duration: 150, transition: 'fade' }` by
        default.

        `transitionProps` is a dict with keys:

        - duration (number; optional):
            Transition duration in ms, `250` by default.

        - exitDuration (number; optional):
            Exit transition duration in ms, `250` by default.

        - keepMounted (boolean; optional):
            If set element will not be unmounted from the DOM when it
            is hidden, `display: none` styles will be applied instead.

        - mounted (boolean; required):
            Determines whether component should be mounted to the DOM.

        - timingFunction (string; optional):
            Transition timing function,
            `theme.transitionTimingFunction` by default.

        - transition (boolean | number | string | dict | list; optional):
            Transition name or object.

    - trapFocus (boolean; optional):
        Determines whether focus should be trapped within dropdown,
        `False` by default.

    - unstyled (boolean; optional):
        Remove all Mantine styling from the component.

    - variant (string; optional):
        variant.

    - width (string | number; optional):
        Dropdown width, or `'target'` to make dropdown width the same
        as target element, `'max-content'` by default.

    - withArrow (boolean; optional):
        Determines whether component should have an arrow, `False` by
        default.

    - withRoles (boolean; optional):
        Determines whether dropdown and target elements should have
        accessible roles, `True` by default.

    - withinPortal (boolean; optional):
        Determines whether dropdown should be rendered within the
        `Portal`, `True` by default.

    - zIndex (string | number; optional):
        Dropdown `z-index`, `300` by default.

- pos (boolean | number | string | dict | list; optional):
    position.

- pr (number; optional):
    paddingRight, theme key: theme.spacing.

- previousIcon (a list of or a singular dash component, string or number; optional):
    Change previous icon.

- previousLabel (string; optional):
    aria-label for previous button.

- ps (number; optional):
    paddingInlineStart, theme key: theme.spacing.

- pt (number; optional):
    paddingTop, theme key: theme.spacing.

- px (number; optional):
    paddingInline, theme key: theme.spacing.

- py (number; optional):
    paddingBlock, theme key: theme.spacing.

- radius (number; optional):
    Key of `theme.radius` or any valid CSS value to set
    `border-radius`, numbers are converted to rem,
    `theme.defaultRadius` by default.

- readOnly (boolean; optional):
    Determines whether the user can modify the value.

- required (boolean; optional):
    Adds required attribute to the input and a red asterisk on the
    right side of label, `False` by default.

- right (string | number; optional)

- rightSection (a list of or a singular dash component, string or number; optional):
    Content section rendered on the right side of the input.

- rightSectionPointerEvents (a value equal to: '-moz-initial', 'inherit', 'initial', 'revert', 'revert-layer', 'unset', 'auto', 'none', 'all', 'fill', 'painted', 'stroke', 'visible', 'visibleFill', 'visiblePainted', 'visibleStroke'; optional):
    Sets `pointer-events` styles on the `rightSection` element,
    `'none'` by default.

- rightSectionProps (dict; optional):
    Props passed down to the `rightSection` element.

- rightSectionWidth (string | number; optional):
    Right section width, used to set `width` of the section and input
    `padding-right`, by default equals to the input height.

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Component size.

- sortDates (boolean; optional):
    Determines whether dates value should be sorted before onChange
    call, only applicable when type=\"multiple\", True by default.

- style (optional):
    Inline style added to root component element, can subscribe to
    theme defined on MantineProvider.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (boolean | number | string | dict | list; optional):
    textAlign.

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional):
    textDecoration.

- top (string | number; optional)

- tt (boolean | number | string | dict | list; optional):
    textTransform.

- type (a value equal to: 'default', 'multiple', 'range'; optional):
    Picker type: range, multiple or default.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- value (string | list of strings; optional):
    Value for controlled component.

- valueFormat (string; optional):
    Dayjs format to display input value, \"MMMM D, YYYY\" by default.

- variant (string; optional):
    variant.

- visibleFrom (boolean | number | string | dict | list; optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional):
    width, theme key: theme.spacing.

- weekdayFormat (string; optional):
    dayjs format for weekdays names, defaults to \"dd\".

- weekendDays (list of a value equal to: 0, 1, 2, 3, 4, 5, 6s; optional):
    Indices of weekend days, 0-6, where 0 is Sunday and 6 is Saturday,
    defaults to value defined in DatesProvider.

- withAsterisk (boolean; optional):
    Determines whether the required asterisk should be displayed.
    Overrides `required` prop. Does not add required attribute to the
    input. `False` by default.

- withCellSpacing (boolean; optional):
    Determines whether controls should be separated by spacing, True
    by default.

- withErrorStyles (boolean; optional):
    Determines whether the input should have red border and red text
    color when the `error` prop is set, `True` by default.

- wrapperProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props passed down to the root element.

- yearLabelFormat (string; optional):
    dayjs label format to display year label or a function that
    returns year label based on year value, defaults to \"YYYY\".

- yearsListFormat (string; optional):
    dayjs format for years list, `'YYYY'` by default."""
    _children_props = ['popoverProps.middlewares.flip.boundary', 'modalProps.title', 'modalProps.overlayProps.children', 'modalProps.closeButtonProps.children', 'modalProps.closeButtonProps.icon', 'leftSection', 'rightSection', 'label', 'description', 'error', 'nextIcon', 'previousIcon']
    _base_nodes = ['leftSection', 'rightSection', 'label', 'description', 'error', 'nextIcon', 'previousIcon', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'YearPicker'
    @_explicitize_args
    def __init__(self, valueFormat=Component.UNDEFINED, disabledDates=Component.UNDEFINED, n_submit=Component.UNDEFINED, debounce=Component.UNDEFINED, id=Component.UNDEFINED, tabIndex=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, hiddenFrom=Component.UNDEFINED, visibleFrom=Component.UNDEFINED, lightHidden=Component.UNDEFINED, darkHidden=Component.UNDEFINED, mod=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ms=Component.UNDEFINED, me=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, ps=Component.UNDEFINED, pe=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bd=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, flex=Component.UNDEFINED, closeOnChange=Component.UNDEFINED, dropdownType=Component.UNDEFINED, popoverProps=Component.UNDEFINED, modalProps=Component.UNDEFINED, clearable=Component.UNDEFINED, clearButtonProps=Component.UNDEFINED, readOnly=Component.UNDEFINED, sortDates=Component.UNDEFINED, labelSeparator=Component.UNDEFINED, placeholder=Component.UNDEFINED, wrapperProps=Component.UNDEFINED, leftSection=Component.UNDEFINED, leftSectionWidth=Component.UNDEFINED, leftSectionProps=Component.UNDEFINED, leftSectionPointerEvents=Component.UNDEFINED, rightSection=Component.UNDEFINED, rightSectionWidth=Component.UNDEFINED, rightSectionProps=Component.UNDEFINED, rightSectionPointerEvents=Component.UNDEFINED, required=Component.UNDEFINED, radius=Component.UNDEFINED, disabled=Component.UNDEFINED, pointer=Component.UNDEFINED, withErrorStyles=Component.UNDEFINED, name=Component.UNDEFINED, label=Component.UNDEFINED, description=Component.UNDEFINED, error=Component.UNDEFINED, withAsterisk=Component.UNDEFINED, labelProps=Component.UNDEFINED, descriptionProps=Component.UNDEFINED, errorProps=Component.UNDEFINED, inputWrapperOrder=Component.UNDEFINED, type=Component.UNDEFINED, value=Component.UNDEFINED, allowDeselect=Component.UNDEFINED, allowSingleDateInRange=Component.UNDEFINED, decadeLabelFormat=Component.UNDEFINED, yearsListFormat=Component.UNDEFINED, size=Component.UNDEFINED, withCellSpacing=Component.UNDEFINED, minDate=Component.UNDEFINED, maxDate=Component.UNDEFINED, numberOfColumns=Component.UNDEFINED, columnsToScroll=Component.UNDEFINED, ariaLabels=Component.UNDEFINED, level=Component.UNDEFINED, nextIcon=Component.UNDEFINED, previousIcon=Component.UNDEFINED, nextLabel=Component.UNDEFINED, previousLabel=Component.UNDEFINED, hasNextLevel=Component.UNDEFINED, yearLabelFormat=Component.UNDEFINED, monthsListFormat=Component.UNDEFINED, monthLabelFormat=Component.UNDEFINED, firstDayOfWeek=Component.UNDEFINED, weekdayFormat=Component.UNDEFINED, weekendDays=Component.UNDEFINED, hideOutsideDates=Component.UNDEFINED, hideWeekdays=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, variant=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowDeselect', 'allowSingleDateInRange', 'aria-*', 'ariaLabels', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearButtonProps', 'clearable', 'closeOnChange', 'columnsToScroll', 'darkHidden', 'data-*', 'debounce', 'decadeLabelFormat', 'description', 'descriptionProps', 'disabled', 'disabledDates', 'display', 'dropdownType', 'error', 'errorProps', 'ff', 'firstDayOfWeek', 'flex', 'fs', 'fw', 'fz', 'h', 'hasNextLevel', 'hiddenFrom', 'hideOutsideDates', 'hideWeekdays', 'inputWrapperOrder', 'inset', 'label', 'labelProps', 'labelSeparator', 'left', 'leftSection', 'leftSectionPointerEvents', 'leftSectionProps', 'leftSectionWidth', 'level', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'maxDate', 'mb', 'me', 'mih', 'minDate', 'miw', 'ml', 'mod', 'modalProps', 'monthLabelFormat', 'monthsListFormat', 'mr', 'ms', 'mt', 'mx', 'my', 'n_submit', 'name', 'nextIcon', 'nextLabel', 'numberOfColumns', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pointer', 'popoverProps', 'pos', 'pr', 'previousIcon', 'previousLabel', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'required', 'right', 'rightSection', 'rightSectionPointerEvents', 'rightSectionProps', 'rightSectionWidth', 'size', 'sortDates', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'type', 'unstyled', 'value', 'valueFormat', 'variant', 'visibleFrom', 'w', 'weekdayFormat', 'weekendDays', 'withAsterisk', 'withCellSpacing', 'withErrorStyles', 'wrapperProps', 'yearLabelFormat', 'yearsListFormat']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'allowDeselect', 'allowSingleDateInRange', 'aria-*', 'ariaLabels', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearButtonProps', 'clearable', 'closeOnChange', 'columnsToScroll', 'darkHidden', 'data-*', 'debounce', 'decadeLabelFormat', 'description', 'descriptionProps', 'disabled', 'disabledDates', 'display', 'dropdownType', 'error', 'errorProps', 'ff', 'firstDayOfWeek', 'flex', 'fs', 'fw', 'fz', 'h', 'hasNextLevel', 'hiddenFrom', 'hideOutsideDates', 'hideWeekdays', 'inputWrapperOrder', 'inset', 'label', 'labelProps', 'labelSeparator', 'left', 'leftSection', 'leftSectionPointerEvents', 'leftSectionProps', 'leftSectionWidth', 'level', 'lh', 'lightHidden', 'lts', 'm', 'mah', 'maw', 'maxDate', 'mb', 'me', 'mih', 'minDate', 'miw', 'ml', 'mod', 'modalProps', 'monthLabelFormat', 'monthsListFormat', 'mr', 'ms', 'mt', 'mx', 'my', 'n_submit', 'name', 'nextIcon', 'nextLabel', 'numberOfColumns', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pointer', 'popoverProps', 'pos', 'pr', 'previousIcon', 'previousLabel', 'ps', 'pt', 'px', 'py', 'radius', 'readOnly', 'required', 'right', 'rightSection', 'rightSectionPointerEvents', 'rightSectionProps', 'rightSectionWidth', 'size', 'sortDates', 'style', 'styles', 'ta', 'tabIndex', 'td', 'top', 'tt', 'type', 'unstyled', 'value', 'valueFormat', 'variant', 'visibleFrom', 'w', 'weekdayFormat', 'weekendDays', 'withAsterisk', 'withCellSpacing', 'withErrorStyles', 'wrapperProps', 'yearLabelFormat', 'yearsListFormat']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(YearPicker, self).__init__(**args)

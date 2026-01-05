# Tail.Blazor.ResponsiveLayout

Independent NuGet package for the TailResponsiveLayout component.

## Installation

```bash
dotnet add package Tail.Blazor.ResponsiveLayout
```

## Features

- Responsive layout container
- Breakpoint-based sizing
- Full theme support with CSS variables
- MAUI Blazor Hybrid compatible

## Class

Component class generated from the Razor file.

## Type Parameters

No generic type parameters.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| ChildContent | RenderFragment? | - | ChildContent parameter |
| LogoTemplate | RenderFragment? | - | LogoTemplate parameter |
| SidebarContent | RenderFragment? | - | SidebarContent parameter |
| AvatarContent | RenderFragment? | - | AvatarContent parameter |
| AppName | string? | - | AppName parameter |
| ShowMenuToggle | bool | true | ShowMenuToggle parameter |
| ShowThemeToggle | bool | true | ShowThemeToggle parameter |
| ShowAvatar | bool | false | ShowAvatar parameter |
| ShowSidebar | bool | true | ShowSidebar parameter |
| ShowHeader | bool | true | ShowHeader parameter |
| StickyHeader | bool | true | StickyHeader parameter |
| HeaderShadow | bool | true | HeaderShadow parameter |
| MenuOpenByDefault | bool | true | MenuOpenByDefault parameter |
| MenuOpenOnMobileByDefault | bool | false | MenuOpenOnMobileByDefault parameter |
| AutoHideOnMobileAfterNavigation | bool | true | AutoHideOnMobileAfterNavigation parameter |
| LayoutMode | LayoutMode | LayoutMode.DrawerLeft | LayoutMode parameter |
| Density | DensityMode | DensityMode.Normal | Density parameter |
| MobileMenuTitle | string? | - | MobileMenuTitle parameter |
| Style | string? | - | Additional CSS styles |
| HideScrollbars | bool | true | HideScrollbars parameter |

## Events

No events exposed.

## Public Properties

| Property | Type | Description |
| --- | --- | --- |
| Dispose | void | Dispose property |

## Methods

No additional public methods.

## Examples

```razor
<TailResponsiveLayout></TailResponsiveLayout>
```
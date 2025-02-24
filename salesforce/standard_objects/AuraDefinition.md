#### AuraDefinition

Represents an Aura component definition, such as component markup, a client-side controller, or an event. This object is available in
API version 32.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Summer ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
AuraDefinitionBundleId
DefType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the bundle containing the definition. A bundle contains a Lightning
definition and all its related resources.

This is a relationship field.

**Relationship Name**
AuraDefinitionBundle

**Relationship Type**
Lookup

**Refers To**
AuraDefinitionBundle

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

```
Format
Source

```

**Description**

The definition type. Valid values are:

**•** `APPLICATION` — Lightning Aura Components app

**•** `CONTROLLER` — client-side controller

**•** `COMPONENT — component markup`

**•** `EVENT` — event definition

**•** `HELPER` — client-side helper

**•** `INTERFACE — interface definition`

**•** `RENDERER — client-side renderer`

**•** `STYLE` — style (CSS) resource

**•** `PROVIDER — reserved for future use`

**•** `MODEL` — deprecated, do not use

**•** `TESTSUITE — reserved for future use`

**•** `DOCUMENTATION` — documentation markup

**•** `TOKENS` — tokens collection

**•** `DESIGN` — design definition

**•** `SVG` — SVG graphic resource

**•** `MODULE` — reserved for future use

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The format of the definition. Valid values are:

**•** `XML` for component markup

**•** `JS` for JavaScript code

**•** `CSS` for styles

**•** `TEMPLATE_CSS` reserved for future use

**•** `SVG` for an SVG graphic

**Type**
textarea

**Properties**
Create, Update

**Description**
The contents of the definition. This is all the markup or code for the definition.


-----

##### Usage

[For more information, see the Lightning Aura Components Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.lightning.meta/lightning/)

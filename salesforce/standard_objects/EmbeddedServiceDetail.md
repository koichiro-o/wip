#### EmbeddedServiceDetail

Represents a metadata catalog object that exposes fields from the underlying Embedded Service setup objects defined in each
EmbeddedServiceConfig deployment for guest users. Guest users don’t have direct access to the Embedded Service setup objects.
Available in API version 39.0 and later.

##### Supported SOAP Calls
```
describeSObjects(), query()

```

-----

##### Supported REST HTTP Methods
```
GET

 Fields

```
```
AvatarImg
ContrastInvertedColor
ContrastPrimaryColor
CustomMinimizedComponent
CustomPrechatComponent

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used as the agent avatar image.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Accent branding color used in the embedded component, displayed as a hexadecimal value.
Changes made to this field in the API aren’t reflected in the embedded component.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value of the `ContrastPrimaryColor field in the EmbeddedServiceBranding setup`
object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The custom Aura component that’s used for the minimized state for this Embedded Chat
deployment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
DurableId
FieldServiceConfirmCardImg
FieldServiceHomeImg
FieldServiceLogoImg
Font
FontSize

```

**Description**
The custom Aura component that’s used for the pre-chat page for this Embedded Chat
deployment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Developer name for the EmbeddedServiceConfig.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the confirmation card in embedded Appointment Management
(beta).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the home screen in embedded Appointment Management (beta).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the logo used for the home screen in embedded Appointment Management (beta).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Font used in the chat text of the Embedded Chat window.

**Type**
picklist


-----

```
HeaderBackgroundImg
Height
IsFieldServiceEnabled
IsLiveAgentEnabled

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Font size for the embedded component.

Possible values are:

**•** Small

**•** Medium

**•** Large

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the header background in Embedded Chat. This field is removed
in API version 49.0 and later. The header background image is no longer supported.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Height of the embedded component.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether Field Service is enabled for this Embedded Service deployment (true)
or not (false). Embedded Appointment Management is currently beta.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether Chat is enabled for this Embedded Service deployment (true) or not
(false).


-----

```
IsOfflineCaseEnabled
IsPrechatEnabled
IsQueuePositionEnabled
NavBarColor
NavBarTextColor
OfflineCaseBackgroundImg

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether offline support is enabled for this Embedded Chat deployment (true)
or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Value of the `PrechatEnabled` field in the EmbeddedServiceLiveAgent setup object.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether queue position (displaying the customer’s place in line while they wait
for an agent) is enabled for this Embedded Chat deployment (true) or not (false).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value of the `NavBarColor` field in the EmbeddedServiceBranding setup object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is used to set the text color for the header.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
PrechatBackgroundImg
PrimaryColor
SecondaryColor
SecondaryNavBarColor
ShouldHideAuthDialog
ShouldShowExistingAppointment

```

**Description**
URL of the image used for the background for the offline support case form in Embedded
Chat.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the background for the pre-chat form in Embedded Chat.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value of the `PrimaryColor` field in the EmbeddedServiceBranding setup object.

**Type**
string

**Properties**
Filter, Group, Nillable Sort

**Description**
Value of the `SecondaryColor` field in the EmbeddedServiceBranding setup object.

**Type**
string

**Properties**
Filter, Group, Nillable Sort

**Description**
This field is used to set the color of a secondary header.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the prompt that the customer log in again during a flow should be hidden
(true) or not (false). When it’s hidden, the customer is taken directly to your login page.

**Type**
boolean


-----

```
ShouldShowNewAppointment
Site
SmallCompanyLogoImg
WaitingStateBackgroundImg
Width

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether to display a button on the home screen for customers to access their
existing appointments (true) or not (false) for embedded Appointment Management
(beta).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether to display a button on the home screen for customers to create a new
appointment (true) or not (false) for embedded Appointment Management (beta).

**Type**
string

**Properties**
Filter, Group, Nillable Sort

**Description**
Value of the `Site` field in the EmbeddedServiceConfig setup object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the logo image used with Embedded Chat.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the background image in Embedded Chat while the customer
waits to be connected with a support agent.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

**Description**
Width of the embedded component.

Note: Any changes you make to the image fields override what you’ve entered in Setup. We recommend setting your image
URLs in Setup.

#### OutOfOffice

```

**Properties**
Create, Nillable

**Description**
Total fee amount, not including taxes.

**Type**
double

**Properties**
Create, Nillable

**Description**
The total fee tax amount.

**Type**
double

**Properties**
Create, Nillable

**Description**
The amount that can be refunded to the client.

**Type**
double

**Properties**
Create, Nillable

**Description**
The total amount of required funds.

**Type**
double

**Properties**
Create, Nillable

**Description**
The combined total of all taxes.


Represents a user-set value on a profile that shows when the user intends to be out of the office. This object is available in API version
41.0 and later.

##### Supported Calls
```
create(), delete(), query(), undelete(), upsert(), update()

```

-----

##### Special Access Rules

In Lightning Experience, lets users set a message next to their name in Chatter to show when they plan to be out of the office. The
message appears in Lightning Experience, Salesforce Classic, and mobile views. Messages expire automatically after their end date. You
can control whether out-of-office functionality is available to your users. Set it up in the Out of Office section in Setup > Chatter Settings.

Only internal users can set an out-of-office message.

##### Fields

```
EndDate
IsEnabled
Message
StartDate

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date of the last day a person is out of the office. After the message expires,
it goes away automatically.

**Type**

boolean

**Properties**
Create, Defaulted on create

**Description**
Indicates whether an out-of-office message can be displayed for a user. The
default value is `true.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The message portion of the out-of-office message. This text, along with start and
end dates, is appended to the user’s name in the Salesforce user interface. The
maximum length of this string is 40 characters.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date of the first day a person is out of the office.


-----

```
UserId

##### Usage

```
**•** Maximum message length is 60 characters.


**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user associated with the out-of-office message.



**•** Users can set only their own out-of-office message. An admin can set an out-of-office message for any user.

**•** The out-of-office message can be set only for internal users.

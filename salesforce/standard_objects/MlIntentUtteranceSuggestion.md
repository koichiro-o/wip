#### MlIntentUtteranceSuggestion

Represents a customer input, used for training purposes in the feedback loop process of a conversation. Admins can add these inputs
to the intent training model. This object is available in API version 51.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
ConfigId
IntentSuggestion
ReviewStatus
Utterance
UtteranceCount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The recommended intent.

**Type**
picklist

**Properties**
Filter, Group, Restricted Picklist, Sort

**Description**
Possible values are: Ignore, New

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The text input from the end user.

**Type**
integer

**Properties**
Filter, Group, Sort


-----

**Description**
A count of the Utterance field.

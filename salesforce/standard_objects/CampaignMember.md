#### CampaignMember

The CampaignMember object represents the relationship between a campaign and either a lead or a contact. If the Accounts as Campaign
Members setting is enabled in an org, CampaignMember can also represent the relationship between a campaign and an account.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
Customer Portal users can’t access this object.

##### Fields

```
AccountId
CampaignId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the account related to the campaign. This field is available only if the Accounts as
Campaign Members setting is enabled in the org.

This field is a relationship field.

**Relationship Name**
Related Record ID

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
City
CompanyOrAccount
ContactId
CurrencyIsoCode

```

**Description**
Required. The ID of the campaign related to the lead or contact.

This field is a relationship field.

**Relationship Name**
Campaign

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city for the address of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the city for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The company or account of the lead or contact.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. The ID of a contact that's related to the campaign.

This field is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist


-----

```
Country
Description
DoNotCall
Email
Fax

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. This field contains
the ISO code for any currency allowed by the organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country for the address of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the country for the account.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the associated lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the description of the account.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the lead or contact doesn’t want to be called. In orgs with the Accounts as
Campaign Members setting enabled, this field can indicate the account doesn’t want to be
called.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for the lead or contact. In orgs with the Accounts as Campaign Members
setting enabled, this field can be the email address for the account.

**Type**
phone


-----

```
FirstName
FirstRespondedDate
HasOptedOutOfEmail
HasOptedOutOfFax
HasResponded

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Fax number for the lead or contact. In orgs with the Accounts as Campaign Members setting
enabled, this field can be the fax number for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name of the lead or contact.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field indicates the date that the campaign member received a status of Responded.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field indicates the email opt-out preference for the lead or contact. A value of `false`
indicates that the lead or contact is opted in to emails. A value of true indicates that they’re
opted out. In orgs with the Accounts as Campaign Members setting enabled, this field can
be the opt-out preference for the account email address.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field indicates the fax opt-out preferences for the lead or contact. A value of false indicates
that the lead or contact is opted in to receiving faxes. A value of true indicates that they’re
opted out. In orgs with the Accounts as Campaign Members setting enabled, this field can
indicate the account has opted out of faxes.

**Type**
boolean


-----

```
LastName
LeadId
LeadOrContactId
LeadOrContactOwnerId

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field indicates whether the campaign member has responded to the campaign (true)
or not (false). Label is Responded.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last name of the lead or contact. The limit is 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. The ID of a lead that's related to the campaign.

This field is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of a lead or contact that's related to the campaign. In orgs with the Accounts as
Campaign Members setting enabled, this field also accepts an account ID.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
LeadSource
MobilePhone
Name
Phone

```

**Description**
The ID of the owner of the associated lead or contact owner. In orgs with the Accounts as
Campaign Members setting enabled, this field can be the owner of the account.

This field is a polymorphic relationship field.

**Relationship Name**
LeadOrContactOwner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The source where the lead was obtained.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile phone number of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the mobile phone number for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first and last name of the lead or contact that's related to the campaign member.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number of the lead or contact. In orgs with the Accounts as Campaign Members
setting enabled, this field can be the phone number for the account.


-----

```
PostalCode
RecordTypeId
Salutation
State
Status

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The postal code for the lead or contact. In orgs with the Accounts as Campaign Members
setting enabled, this field can be the postal code for the account.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object. To change the record type, modify the
`CampaignMemberRecordTypeId` field on the associated Campaign.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salutation for the lead or contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The state for the address of the lead or contact. The limit is 80 characters. In orgs with the
Accounts as Campaign Members setting enabled, this field can be the state of the account
address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Controls the `HasResponded` flag on this object. You can't directly set the
`HasResponded` flag, as it’s read-only. You can set it indirectly by setting this field in a
create or update call. Each predefined value implies a `HasResponded` flag value. Each
time you update this field, you implicitly update the HasResponded flag. In the Salesforce
user interface, Marketing users can define valid status values for the `Status` picklist. They


-----

```
Street
Title
Type

```

can choose one status as the default status. For each `Status` field value, they can also
select which values to count as “Responded,” meaning that the `HasResponded flag is`
set to `true` for those values. The limit is 40 characters.

When you create or update campaign members, use the text value for `Status` instead of
the ID from the CampaignMemberStatus object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street for the address of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the street of the account address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Title for the lead or contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates if the campaign member is a lead or a contact. In orgs with the Accounts as
Campaign Members setting enabled, this field can indicate an account.


Note: If you’re importing CampaignMember data into Salesforce and want to set the value for an audit field, such as
```
  CreatedDate, contact Salesforce. Audit fields are automatically updated during API operations unless you request to set these

```
fields yourself.

##### Usage

Each record has a unique ID, and must contain either a `ContactId` or a `LeadId, but can't contain both. Any attempt to create a`
single record with both results in a successful insert but only the ContactId is inserted. However, you can create two separate records
on a Campaign—one for the Lead and one for the Contact.

In orgs with the Accounts as Campaign Members setting enabled, the unique ID can be an `AccountID.`


-----

Standard fields from a lead or contact are associated with the CampaignMember object, but you can’t query them directly. To include
a `Phone` in your query, for example, query the field from the Lead object.
```
SELECT Id, (SELECT Phone FROM Lead)
FROM CampaignMember

```
This object is defined only for orgs that have the marketing feature and valid marketing licenses. If your org doesn’t have the marketing
feature or valid marketing licenses, this object doesn’t appear in the `describeGlobal()` call, and you can't use
`describeSObjects()` or `query()` with this object.

Note: If you want to track lead-based campaign members you convert to contacts, provide both a ContactId and a LeadId.
Otherwise, only use one ID type.

To issue `create()` requests to the API, your account only requires read access to campaigns.

If the record doesn’t exist for the specified `ContactId` or `LeadId, then a new record is created. If the record exists, an error is`
returned and no update is made. To update an existing record, specify the ID of the CampaignMember record to update.

To delete a record, specify the ID of the CampaignMember record.

When creating or updating records, the `Status` field value specified in the call is verified as a valid status for the given Campaign:

**•** If the specified `Status` value is a valid status, the value is updated, and the `HasResponded` field is updated to either `true`
or `false, depending on the` `Status` value association with `HasResponded.`

**•** If the specified `Status` value isn’t a valid status, the API assigns the default status to the `Status` field and updates the
`HasResponded` field with the associated value. However, if the given Campaign doesn’t have a default status, the API assigns
the value specified in the call to the `Status` field, and the `HasResponded` field is set to `false.`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CampaignMemberChangeEvent (API version 46.0)**
Change events are available for the object.

SEE ALSO:

Campaign

CampaignMemberStatus

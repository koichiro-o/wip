#### ConversationVendorInfo

This setup object connects the partner vendor system to the Service Cloud feature. For example, for Service Cloud Voice, this object
contains information about the partner telephony or Contact Center as a Service (CCaaS) partner system. For Bring Your Own Channel
this object contains information about the partner messaging system, and for Bring Your Own Channel for CCaaS, this object contains
information about the CCaaS partner system. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
This object requires an add-on license for Service Cloud Voice for Partner Telephony or Digital Engagement.


-----

##### Fields

The fields in the ConversationVendorInfo object apply to all Service Cloud features unless otherwise stated in the field description. For
example, if a field applies to just one Service Cloud Voice telephony model setup or is applied differently by different partner systems,
this is stated in the field description.

|Field|Details|
|---|---|
|AwsAccountKey|Type string Properties Create, Filter, Group, Nillable, Sort, Update Description The 12-digit AWS subaccount ID that’s automatically provisioned for you when Service Cloud Voice was turned on. Available in API version 55.0 and later. Applies to the following implementation: • Service Cloud Voice with Amazon Connect|
|AwsRootEmail|Type email Properties Create, Filter, Group, Nillable, Sort, Update Description The email address used by Salesforce to create the root user for the provisioned AWS subaccount when Service Cloud Voice was turned on. Available in API version 55.0 and later. Applies to the following implementation: • Service Cloud Voice with Amazon Connect|
|AwsTenantVersion|Type double Properties Create, Filter, Nillable, Sort, Update Description The version number of the SVCTenantStack AWS CloudFormation stack that’s deployed. The stack is deployed in AWS region "us-east-1". Available in API version 55.0 and later. Applies to the following implementation: • Service Cloud Voice with Amazon Connect|
|agentSSOSupported|Type boolean Properties Create, Filter, Group, Update|


-----

|Field|Details|
|---|---|
||Description If set to true, agents can single sign-on (SSO) into their contact center using Salesforce as the identity provider (IdP). Behind the scenes, Salesforce is used as the SAML IdP in the Single Sign-On connected app for the contact center. If set to false, an IdP other than Salesforce is used or an IdP isn’t used at all. The default value is false. If this value is set to false and you want to use Salesforce as the IdP for your contact center, set this value and the namedCredentialSupported value to true and configure the service_cloud_voice.PartnerSSO interface in your Apex integration class. Available in API version 53.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|BridgeComponent|Type string Properties Create, Filter, Group, Nillable, Sort, Update Description The Lightning component used to communicate between the telephony or messaging system and other Lightning components. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|CapabilitiesSupportsIntelligence|Type boolean Properties Create, Filter, Update Description If set to true, Salesforce ingests real-time signals sent from a partner telephony system. If set to false, Salesforce doesn't ingest real-time intelligence signals from a partner telephony system. The default value is false. Available in API version 59.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony|
|CapabilitiesSupportsKeyProvisioning|Type boolean Properties Create, Filter, Update|


-----

|Field|Details|
|---|---|
||Description If set to true, Salesforce has permission to automatically provision public keys to contact centers. The default value is false. Available in API version 54.0 and later. Applies to the following implementation: • Service Cloud Voice with Partner Telephony|
|CapabilitiesSupportsPartnerPhoneNumbers|Type boolean Properties Create, Filter, Update Description If set to true, Salesforce has permission to access relevant agents’ phone numbers while configuring contact center channels. The default value is false. Available in API version 54.0 and later. Applies to the following implementation: • Service Cloud Voice with Partner Telephony|
|CapabilitiesSupportsQueueManagement|Type boolean Properties Create, Filter, Update Description If set to true, support queue management. The default value is false. Available in API version 56.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|CapabilitiesSupportsUnifiedRouting (Beta)|Type boolean Properties Create, Filter, Update Description Indicates whether unified routing is supported (true) or not supported (false) for inbound voice calls in voice channels. The default value is false. Once this value is set to true, it can’t be changed to false. Available in API version 63.0 and later. Applies to the following implementation:|


-----

|Field|Details|
|---|---|
||• Service Cloud Voice with Partner Telephony|
|ClientAuthMode|Type picklist Properties Create, Filter, Group, Restricted picklist, Sort, Update Description The client authentication mode. Possible values are: • Custom • Mixed • SSO Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect|
|ConnectorUrl|Type url Properties Create, Filter, Group, Sort, Update Description The URL that hosts your Service Cloud Voice or Bring Your Own Channel for CCaaS connector. This value could be a Visualforce page or a public URL. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|customConfig|Type CustomEntityDefinition Properties Create, Filter, Group, Update Description The foreign key to the CustomEntityDefinition, which contains partner-specific custom settings. Available in API version 53.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|


-----

|Field|Details|
|---|---|
|CustomIconId|Type reference Properties Filter, Group, Nillable, Sort Description ID of the static resource used to identify the contact center integration, such as a Contact Center as a Service (CCaaS) provider logo. The static resource must be in SVG format. This field is optional. Available in API version 62.0 and later. This field is a relationship field. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Bring Your Own Channel for CCaaS This field is a relationship field. Relationship Name CustomIcon Refers To StaticResource|
|CustomLoginUrl|Type url Properties Create, Filter, Group, Nillable, Sort, Update Description The URL that hosts your telephony system or CCaaS system login page. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|DeveloperName|Type string Properties Create, Filter, Group, Sort, Update Description The unique name of the object in the API. Note: Only users with View DeveloperName or View Setup and Configuration permissions can view, group, sort, and filter this field.|
|IsTaxCompliant|Type string|


-----

|Field|Details|
|---|---|
||Properties Create, Defaulted on create, Filter, Group, Sort, Update Description Indicates whether the Amazon tax settings for the AWS subaccount provisioned for Service Cloud Voice have been confirmed (true). The default value is false. Available in API version 55.0 and later. Applies to the following implementation: • Service Cloud Voice with Amazon Connect|
|einsteinConversationInsights Supported|Type boolean Properties Create, Filter, Group, Update Description If set to true, Einstein Conversation Insights is turned on. The default value is false. Available in API version 53.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect|
|integrationClass|Type ApexClass Properties Create, Filter, Group, Update Description The foreign key to the partner Apex class implementing supported interfaces. Available in API version 53.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|IntegrationClassName|Type string Properties Create, Filter, Group, Nillable, Sort, Update Description Deprecated in API version 53.0. Don't set this field. Instead, use integrationClass. Applies to the following implementations: • Service Cloud Voice with Partner Telephony|


-----

|Field|Details|
|---|---|
||• Service Cloud Voice with Partner Telephony from Amazon Connect|
|keyProvisioningSupported|Type boolean Properties Create, Filter, Group, Update Description If set to true, key provisioning and renewal are automated. The default value is false. Available in API version 54.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect|
|Language|Type picklist Properties Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update Description The language of the master label (MasterLabel) in the user interface. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|MasterLabel|Type string Properties Create, Filter, Group, Sort, Update Description The partner vendor's display name as it appears in the UI. This name appears in several places in the UI, so include the partner vendor name for easy identification. For Service Cloud Voice, this label also represents the telephony provider name in the contact center record. For Service Cloud Voice with Amazon Connect, this field is always set to Service Cloud Voice.|
|namedCredential|Type Named Credential Properties Create, Filter, Group, Update|


-----

|Field|Details|
|---|---|
||Description A sample-named credential that can be used for Apex callouts to the partner system. Available in API version 53.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|namedCredentialSupported|Type boolean Properties Create, Filter, Group, Update Description If set to true and if supported by the partner telephony, then prescriptive setup through a named credential is enabled allowing server-to-server communication with a named credential. Available in API version 53.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|NamespacePrefix|Type string Properties Filter, Group, Nillable, Sort Description The namespace prefix that’s associated with this object. Applies to the following implementations: • Service Cloud Voice with Amazon Connect • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|partnerContactCenterList Supported|Type boolean Properties Create, Filter, Group, Update|


-----

|Field|Details|
|---|---|
||Description If set to true, enables the customer to select one contact center from a list of multiple contact centers to connect with Salesforce. The default value is false. Available in API version 53.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|partnerPhoneNumbersSupported|Type boolean Properties Create, Filter, Group, Update Description If set to true, displays a list of phone numbers used to create contact center channels. The default value is false. Available in API version 54.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect|
|partnerTransfer DestinationsSupported|Type boolean Properties Create, Filter, Group, Update Description If set to true, allows Salesforce to fetch contact center queues so that Salesforce and contact center queues can be mapped. The default value is false. Available in API version 53.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect • Bring Your Own Channel for CCaaS|
|ServerAuthMode|Type picklist Properties Create, Filter, Group, Restricted picklist, Sort, Update Description Deprecated in API 53.0. Server authentication mode. Set this value to None. Applies to the following implementations:|


-----

|Field|Details|
|---|---|
||• Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect|
|TelephonySettingsComponent|Type string Properties Create, Filter, Group, Nillable, Sort, Update Description The name of the Lightning Web Component (LWC) that is used to display additional agent settings in the Omni-Channel widget. This value is in the format mynamespace:componentName, where mynamespace is the namespace associated with the Service Cloud Voice package that was created, and componentName is the FQDN of the Lightning component. Available in API version 54.0 and later. Applies to the following implementation: • Service Cloud Voice with Partner Telephony|
|universalCallRecording AccessSupported|Type boolean Properties Create, Filter, Group, Update Description If set to true, Universal Call Recording Access is turned on. The default value is false. If this value is set to false and you want to turn on Universal Call Recording, set this value to true and configure the service_cloud_voice.RecordingMediaProvider interface in your Apex integration class. Available in API version 54.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect|
|userSyncingSupported|Type boolean Properties Create, Filter, Group, Update Description If set to true, supports automated user syncing whenever a user is added to or removed from a contact center. The default value is false. Available in API version 53.0 and later. Applies to the following implementations: • Service Cloud Voice with Partner Telephony • Service Cloud Voice with Partner Telephony from Amazon Connect|


-----

|Field|Details|
|---|---|
||• Bring Your Own Channel for CCaaS|
|vendorType|Type picklist Properties Create, Filter, Group, Update Description The Service Cloud feature the partner vendor supports. Possible values are: • Amazon_Connect — For Service Cloud Voice with Amazon Connect. • BringYourOwnChannelPartner — For Bring Your Own Channel. Available in API version 60.0 and later. • BringYourOwnContactCenter — For Bring Your Own Channel for Contact Center as a Service (CCaaS). Available in API version 60.0 and later. • ServiceCloudVoicePartner — For Service Cloud Voice with Partner Telephony or Service Cloud Voice with Partner Telephony from Amazon Connect. If you're inserting or updating the record, this field must be set. Available in API version 53.0 and later.|


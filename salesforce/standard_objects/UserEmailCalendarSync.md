#### UserEmailCalendarSync

Represents the user assignments of an Einstein Activity Capture configuration. This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), describeSObjects(), query(), update(), upsert()

 Special Access Rules

```
To access this object, enable Einstein Activity Capture in your org.

##### Fields

```
AssignedId
ConfigurationId

##### Usage

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user or profile. Only Einstein Activity users can be added to a configuration.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Einstein Activity Capture configuration. The configuration is created in Salesforce
Setup. After the configuration is created, the autogenerated ID is visible on the Configurations
tab. From Setup, in the Quick Find box, enter `Einstein Activity Capture, and`
then select Settings. Click the Configurations tab.


Use UserEmailCalendarSync to add and remove users to an Einstein Activity Capture configuration. You can add users to a configuration
via a user ID or a profile ID. You can add a profile to only one configuration and assign a profile to only one user.


-----

This example adds two users to an Einstein Activity Capture configuration.
```
// Create a list of UserEmailCalendarSync records
List<UserEmailCalendarSync> usersToAdd = new ArrayList<>();
// Populate the UserEmailCalendarSync record with the ID of
// the user or profile, and with the ID of the Activity Capture configuration you are
adding them to
UserEmailCalendarSync user1 = new UserEmailCalendarSync(ConfigurationId = '0063xxxxxxxxxxx',
 AssignedId = '005xxxxxxxxxxxx');
UserEmailCalendarSync user2= new UserEmailCalendarSync(ConfigurationId = '0063xxxxxxxxxxx',
 AssignedId = '005xxxxxxxxxxxx');
// add the UserEmailCalendarSync users to your list
usersToAdd.add(user1);
usersToAdd.add(user2);
// Insert the list of UserEmailCalendarSync into the database
Database.SaveResult[] results = Database.insertImmediate(usersToAdd);

```
This example removes a user from an Einstein Activity Capture configuration.

To remove a user, call `UserEmailCalendarSync(), passing in` `null` for `ConfigurationId.`
```
UserEmailCalendarSync user2Remove= new UserEmailCalendarSync(ConfigurationId = "", AssignedId
 ='005xxxxxxxxxxxx');
Database.SaveResult results =Database.insertImmediate(user2Remove);

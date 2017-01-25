Canadian Forces Base Skins

Adds new skins for the base ARMA units inspired by Canadian Armed Forces.

Check out the project at: https://github.com/astruyk/CFB_Skins for more information.

Changelog
3.0.1
* Fixed an error that popped up on startup with CFB_Skins loaded
* Fixed a number of RPT errors related to incorrect inheritance definitions in CfgWeapons
* Fixed a few pop-up errors that would occur when placing JTF-2 units in Eden/Zeus
* Fixed custom skin not showing correctly for CH-147 Chinook
* Fixed some inconsistent naming for RCAF aircraft (now uses 'Transport' or 'Armed' to consistently)
* Fixed some vehicles not showing up in the Arsenal Garage

3.0.0
* Support for spawning units in ALiVE. Units are sorted as follows:
  * Note - this includes a number of group/unit changes and is breaking for existing missions. Hopefully this will be the last time.
  * Canadian Forces (AR)
  * Canadian Forces (TW)
  * Canadian Special Operations Forces Command
  * Royal Canadian Air Force
  * Rebels
* Add red-cross medic patch in unit insignia (not yet added to medic roles but can be used in Arsenal)
* Add some canadian flags:
  * Canadian Flag
  * Canadian Armed Forces
  * Canadian Army
  * Royal Canadian Navy
  * Royal Canadian Air Force
  * Royal Canadian Military College (Kingston)
  * Royal Canadian Military College (Saint-Jean)

2.4.1
* Support RHS AK's for Rebels (in addition to CUP and HLC weapons).
* Fix an RPT error with rebel sniper unit due to incorrect uniform.

2.4.0
* Add 2 variants of the CH-147 Chinook (Armed & Unarmed)
* Add CADPAT TW and CADPAT AR variants of the ECH helmet

2.3.1
* CADPAT and JTF2 items now show up in Zeus when editing ammo boxes.
* Rebels will now also attempt to switch to using AK's + RPK's from @CUP mod if HLC isn't present.

2.3.0 - LSSV's
* Added unarmed Light Service Support Vehicles (LSSV).
* Added armed Light Service Support Vehicles (LSSV).
* Fix issue where AR uniforms weren't showing when adding items to Arsenal through Zeus

2.2.0 - CADPAT AR
* Added CADPAT AR variants for all existing CADPAT TW units, equipment, and groups.

2.1.0 - Rebels!
* Added new 'Rebels' faction to OPFOR with lightly armed zeus-compatible units built from existing ARMA uniforms including:
  * 13 Kinds of infantry unit
  * 3 Vehicles (Armed and unarmed technicals, quadbikes)
  * 7 static weapons (2xHMG, 2xGMG, Mortars, AT, AA)
* Added groups for 'Rebels' factions:
  * 8 kinds of infantry group
  * 2 Vehicle Groups
  * 3 Mechanized Groups
* Rebel units will (sometimes) be equipped with AK-47's if the HLC AK mod is detected

2.0.1
* Populate backpacks for units with appropriate equipment
* Add optics and attachments to default unit setups
* Add unique icons for all of the equipment
* Fix typo in CADPAT uniform names where they were showing as 'CADPAD' instead
* Use more appropriate backpack camo for units needing carryalls (most AT/AA ammobearers)
* Fix some issues with uneccessarily overridden uniform weights and volumes (now they inherit from the base class correctly)
* Fix an issue where there was a JTF2 member in one of the CADPAT TW groups
* JTF2 units have balaclavas by default now
* JTF2 units have some unique equipment now (silencers, tan rifles, different optics)

2.0.0
* Incremented version number to 2.0.0 because of class name changes which would break existing missions.
* Completely re-did the CADPAT TW texture to include more detail based on real-world samples instead of digital approximation
* Added new JTF2 faction with black themed uniforms and helmets
* Added a lot of new units with CADPAT TW & JTF2 setups:
  * Rifleman (AT)
  * Ammobearer (Rifle/AT/AA/AR/MMG)
  * Missile Specialist (AT)
  * Missile Specialist (AA)
  * Engineer
* Added groups for CADPAT TW & JTF2 setups:
  * Rifle Section (8 men)
  * Rifle Assault Group (4 men)
  * Support Assault Group (4 men)
  * Marksman Team (2 men)
  * MMG Weapons Group (3 men)
  * AT Missile Group (3 men)
  * AA Missile Group (3 men)
  * Engineer Group  (3 men)
  * Sentry Team (2 men)
* Modified some existing unit display names to match the ones in vanilla arma
* A bunch of unit definition cleanup (mostly behind the scenes stuff, but names should be final now)
* Fixed some units not showing up correctly in Zeus

1.0.1
* Signed addon with unique key (not debug key)

1.0.0
* Added CADPAT Temperate Woodland skinned equipment:
  * Added CADPAT Combat Uniform
  * Added CADPAT Combat Uniform (Rolled Up)
  * Added CADPAT Combat Uniform (Tee)
  * Added CADPAT TW Assault Backpack
  * Added CADPAT TW Kitbag
  * Added CADPAT TW Tactical Vest
  * Added CADPAT TW Plate Carrier Lite
  * Added CADPAT TW Plate Carrier
* Added RCAF skinned equipment:
  * Added RCAF Flight Coveralls
* Added RCAF skinned vehicles:
  * Added CH-148 Cyclone
  * Added CH-146 Griffon
* Added 'Canadian Armed Forces' faction:
  * Added 'RCAF' class to CAF faction
  * Added 'CADPAT TW' class to CAF faction
* Added new units to CAF section based on NATO counterparts but using CADPAT skin variants:
  * Rifleman
  * Section Leader
  * Automatic Rifleman
  * Marksman
* Added new units to RCAF section based on NATO counterparts but using CADPAT skin variants:
  * Helicopter Pilot
  * Helicopter Crew
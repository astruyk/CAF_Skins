import re;

# Some regex's to help when processing.
preprocessorDefinition = re.compile('class [\w]+;');
classNameRegex = re.compile('class ([\w]+) : [\w]+');

# Generate a copy of the TW units configured for JTF2
inputFileName = "../src/@CFB_Skins/addons/cfb_skins/vehicles_units_tw.hpp";
outputFileName = "../src/@CFB_Skins/addons/cfb_skins/vehicles_units_jtf2.hpp";
with open(inputFileName, 'r') as inputFile:
	with open(outputFileName, 'w') as outputFile:
		currentClassName = "";
		indentDepth = 0;
		for line in inputFile:
			shouldBeCommentedOut = False;
			if preprocessorDefinition.match(line):
				shouldBeCommentedOut = True;
			classNameMatch = classNameRegex.match(line);
			if (classNameMatch):
				currentClassName = classNameMatch.group(1);
			
			if "{" in line:
				indentDepth += 1;
			if "}" in line:
				indentDepth -= 1;

			# Transform the base class name from a TW solder to a JTF2 soldier
			line = line.replace("CFB_TW_Soldier", "CFB_JTF2_Soldier");
			
			# Change the base vehicle class so they show up in the JTF2 section
			line = line.replace("CFB_TW_VehicleClass", "CFB_JTF2_VehicleClass");
			
			# Map the uniforms from TW -> JTF2. Also make sure the skin file is selected correctly.
			line = line.replace("CFB_TW_Uniform", "CFB_JTF2_Uniform");
			line = line.replace("CFB_TW_Rolled_Uniform", "CFB_JTF2_Rolled_Uniform");
			line = line.replace("CFB_TW_Tshirt_Uniform", "CFB_JTF2_Rolled_Uniform"); # TMP remove all of the T-shirt loadouts with the rolled arms one. The stupid undershirt looks dumb.
			line = line.replace("\cfb_skins\CADPAT_TW_Uniform_NATO.paa", "\cfb_skins\JTF2_Uniform_NATO.paa");
			
			# Change some of the equipment the unit starts with
			line = line.replace("NVGoggles_INDEP", "NVGoggles_OPFOR");
			line = line.replace("CFB_TW_Helmet", "CFB_JTF2_Helmet");
			line = line.replace("CFB_TW_Boonie", "CFB_JTF2_Helmet"); # TMP - need alternate hat to boonie
			line = line.replace("CFB_TW_Patrol", "CFB_JTF2_Helmet"); # TMP - need alternate hat to patrol
			line = line.replace("CFB_TW_Backpack_Assault", "B_AssaultPack_blk");
			line = line.replace("\"CFB_TW_Backpack_Kitbag\"", "\"B_Kitbag_rgr\"");
			line = line.replace("CFB_TW_Vest_Tactical", "V_TacVestIR_blk");
			
			# Change the weapons to silenced versions
			line = line.replace("CFB_MX_Black_MRCO", "arifle_MX_ACO_pointer_snds_F");
			line = line.replace("CFB_MXM_Black_SOS", "arifle_MXM_RCO_pointer_snds_F");
			line = line.replace("CFB_MX_GL_Black_MRCO", "arifle_MX_GL_Holo_pointer_snds_F");
			line = line.replace("CFB_MXC_Black_MRCO", "arifle_MXC_Holo_pointer_snds_F");
			
			# Add some extra linked items
			line = line.replace("linkedItems[] = {", "linkedItems[] = { \"G_Balaclava_blk\",");
			
			# HACK - MMG and AR gunners should get a different vest since there is no BIS black PlateCarrier2 equivalent.
			if "Soldier_MMG" in currentClassName or "Soldier_AR" in currentClassName:
				line = line.replace("CFB_TW_Vest_PlateCarrier1", "V_Chestrig_blk");
				line = line.replace("CFB_TW_Vest_PlateCarrier2", "V_Chestrig_blk");
			else:
				line = line.replace("CFB_TW_Vest_PlateCarrier1", "V_PlateCarrier1_blk");
				line = line.replace("CFB_TW_Vest_PlateCarrier2", "V_PlateCarrier1_blk"); # TODO we need an alternative for the plate carrier 2.

			if shouldBeCommentedOut:
				outputFile.write("// ");
			outputFile.write(line);

# Generate equivalent groups for JTF2 units
inputFileName = "../src/@CFB_Skins/addons/cfb_skins/groups_tw.hpp";
outputFileName = "../src/@CFB_Skins/addons/cfb_skins/groups_jtf2.hpp";
with open(inputFileName, 'r') as inputFile:
	with open(outputFileName, 'w') as outputFile:
		for line in inputFile:

			# Transform the base class name from TW groups to JTF2 groups
			line = line.replace("CFB_Groups_CADPAT_TW", "CFB_Groups_JTF2");
			
			# Change the section names
			line = line.replace("Infantry (CADPAT TW)", "Infantry (JTF2)");
			
			# Change the names of the units
			line = line.replace("CFB_TW_Soldier", "CFB_JTF2_Soldier");

			outputFile.write(line);
			
# Generate equivalent backpacks for JTF2 units
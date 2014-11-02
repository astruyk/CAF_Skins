class CFB_Groups_CADPAT_TW
{
	name = "Infantry (CADPAT TW)";
	class CFB_Groups_CADPAT_TW_Rifle_Section
	{
		faction = "CFB_Base_Faction";
		name = "Rifle Section";
		side = 1;

		class Unit0 { side = 1; vehicle = "CFB_TW_Soldier_TL"; rank = "SERGEANT"; position[] = {0,0,0}; };
		class Unit1 { side = 1; vehicle = "CFB_TW_Soldier_GL"; rank = "PRIVATE"; position[] = {5,-5,0}; };
		class Unit2 { side = 1; vehicle = "CFB_TW_Soldier_AR"; rank = "PRIVATE"; position[] = {-5,-5,0}; };
		class Unit3 { side = 1; vehicle = "CFB_TW_Soldier"; rank = "PRIVATE"; position[] = {10,-10,0}; };
		
		class Unit4 { side = 1; vehicle = "CFB_TW_Soldier_TL"; rank = "CORPORAL"; position[] = {-10,-10,0}; };
		class Unit5 { side = 1; vehicle = "CFB_TW_Soldier_Medic"; rank = "PRIVATE"; position[] = {15,-15,0}; };
		class Unit6 { side = 1; vehicle = "CFB_TW_Soldier_AR"; rank = "PRIVATE"; position[] = {-15,-15,0}; };
		class Unit7 { side = 1; vehicle = "CFB_TW_Soldier_Marksman"; rank = "PRIVATE"; position[] = {20,-20,0}; };
	};
	
	class CFB_Groups_CADPAT_TW_Rifle_Assault_Team
	{
		faction = "CFB_Base_Faction";
		name = "Rifle Assault Group";
		side = 1;

		class Unit0 { side = 1; vehicle = "CFB_TW_Soldier_TL"; rank = "SERGEANT"; position[] = {0,0,0}; };
		class Unit1 { side = 1; vehicle = "CFB_TW_Soldier_GL"; rank = "PRIVATE"; position[] = {5,-5,0}; };
		class Unit2 { side = 1; vehicle = "CFB_TW_Soldier_AR"; rank = "PRIVATE"; position[] = {-5,-5,0}; };
		class Unit3 { side = 1; vehicle = "CFB_TW_Soldier"; rank = "PRIVATE"; position[] = {10,-10,0}; };
	};
	
	class CFB_Groups_CADPAT_TW_Support_Assault_Team
	{
		faction = "CFB_Base_Faction";
		name = "Support Assault Group";
		side = 1;

		class Unit0 { side = 1; vehicle = "CFB_TW_Soldier_TL"; rank = "SERGEANT"; position[] = {0,0,0}; };
		class Unit1 { side = 1; vehicle = "CFB_TW_Soldier_Medic"; rank = "PRIVATE"; position[] = {5,-5,0}; };
		class Unit2 { side = 1; vehicle = "CFB_TW_Soldier_AR"; rank = "PRIVATE"; position[] = {-5,-5,0}; };
		class Unit3 { side = 1; vehicle = "CFB_TW_Soldier_Marksman"; rank = "PRIVATE"; position[] = {10,-10,0}; };
	};
	
	class CFB_Groups_CADPAT_TW_Marksman_Team
	{
		faction = "CFB_Base_Faction";
		name = "Marksman Team";
		side = 1;

		class Unit0 { side = 1; vehicle = "CFB_TW_Soldier_TL"; rank = "CORPORAL"; position[] = {0,0,0}; };
		class Unit1 { side = 1; vehicle = "CFB_TW_Soldier_Marksman"; rank = "PRIVATE"; position[] = {5,-5,0}; };
	};
	
	class CFB_Groups_CADPAT_TW_MMG_Team
	{
		faction = "CFB_Base_Faction";
		name = "MMG Weapon Group";
		side = 1;

		class Unit0 { side = 1; vehicle = "CFB_TW_Soldier_MMG"; rank = "CORPORAL"; position[] = {0,0,0}; };
		class Unit1 { side = 1; vehicle = "CFB_TW_Soldier"; rank = "PRIVATE"; position[] = {5,-5,0}; };
		class Unit2 { side = 1; vehicle = "CFB_TW_Soldier"; rank = "PRIVATE"; position[] = {-5,-5,0}; };
	};
};

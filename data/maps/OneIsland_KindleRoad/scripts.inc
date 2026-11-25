OneIsland_KindleRoad_MapScripts::
	.byte 0

OneIsland_KindleRoad_EventScript_RouteSign::
	msgbox OneIsland_KindleRoad_Text_RouteSign, MSGBOX_SIGN
	end

OneIsland_KindleRoad_EventScript_EmberSpaSign::
	msgbox OneIsland_KindleRoad_Text_EmberSpaSign, MSGBOX_SIGN
	end


SerraRoute_EventScript_Researcher::
	lock
	faceplayer
	msgbox SerraRoute_Text_Researcher, MSGBOX_NPC
	release
	end

SerraRoute_EventScript_Sign::
	msgbox SerraRoute_Text_Sign, MSGBOX_SIGN
	end

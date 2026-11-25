VilaFlocos_MapScripts::
    .byte 0

VilaFlocos_EventScript_Sign::
    msgbox VilaFlocos_Text_Sign, MSGBOX_SIGN
    end

VilaFlocos_EventScript_Researcher::
    lock
    faceplayer
    goto_if_set FLAG_SERRA_STARTER_GIVEN, VilaFlocos_EventScript_AlreadyGotStarter
    msgbox VilaFlocos_Text_Researcher, MSGBOX_DEFAULT
    givemon SPECIES_SNOLET, 5
    setflag FLAG_SERRA_STARTER_GIVEN
    setflag FLAG_SYS_POKEMON_GET
    msgbox VilaFlocos_Text_ReceivedSnolet, MSGBOX_DEFAULT
    release
    end

VilaFlocos_EventScript_AlreadyGotStarter::
    msgbox VilaFlocos_Text_AlreadyGotStarter, MSGBOX_NPC
    release
    end

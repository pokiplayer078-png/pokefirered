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

VilaFlocos_EventScript_Lugia::
    lock
    faceplayer
    goto_if_set FLAG_SERRA_LUGIA_CALLED, VilaFlocos_EventScript_LugiaAlreadyObtained
    msgbox VilaFlocos_Text_Lugia, MSGBOX_DEFAULT
    givemon SPECIES_LUGIA_S, 50
    setflag FLAG_SERRA_LUGIA_CALLED
    msgbox VilaFlocos_Text_LugiaReceived, MSGBOX_DEFAULT
    release
    end

VilaFlocos_EventScript_LugiaAlreadyObtained::
    msgbox VilaFlocos_Text_LugiaAlready, MSGBOX_NPC
    release
    end

VilaFlocos_EventScript_HoOh::
    lock
    faceplayer
    goto_if_set FLAG_SERRA_HO_OH_REVIVED, VilaFlocos_EventScript_HoOhAlreadyRevived
    msgbox VilaFlocos_Text_HoOh, MSGBOX_DEFAULT
    checkitem ITEM_MAX_REVIVE, 10
    goto_if_eq VAR_RESULT, 0, VilaFlocos_EventScript_HoOhNeedItems
    removeitem ITEM_MAX_REVIVE, 10
    setflag FLAG_SERRA_HO_OH_REVIVED
    msgbox VilaFlocos_Text_HoOhRevived, MSGBOX_DEFAULT
    givemon SPECIES_HO_OH_C, 50
    msgbox VilaFlocos_Text_HoOhCaptured, MSGBOX_DEFAULT
    release
    end

VilaFlocos_EventScript_HoOhNeedItems::
    msgbox VilaFlocos_Text_HoOhNeedItems, MSGBOX_DEFAULT
    release
    end

VilaFlocos_EventScript_HoOhAlreadyRevived::
    msgbox VilaFlocos_Text_HoOhAlready, MSGBOX_NPC
    release
    end

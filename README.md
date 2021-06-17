<details>
  <summary>Abbreviations <sup>(toggle)</sup></summary>
  <pre>
  | Abbreviation | note          | Meaning                                    |
  | ---          | ---           | ---                                        |
  | "OMEMO"      | (with quotes) | refers to the official "OMEMO" plugin.     |
  | "OMEMO Mod"  | (with quotes) | refers to the present modified version.    |
  | OMEMO        | acronym       | refers to the XMPP Extension Protocol.     |
  | (ext)        |               | external hyperlink (immediately preceding) |
  | ref          |               | reference                                  |
  | DEV          |               | software development                       |
  | SecOps       |               | Security Operations [1]                    |
  </pre>
  <sup>[1] https://www.vmware.com/topics/glossary/content/secops</sup>
</details>

---


# "OMEMO Mod" plugin for Gajim

A modified version of the official OMEMO plugin for Gajim that exposes the "unacknowledged message count" (`UNACKNOWLEDGED_COUNT`) and the rest of the `backend.utils` constants as user configurable values. It works as a drop-in replacement.

These additional settings can be found in the "Advanced" section under the "Settings" tab of the "OMEMO configuration" panel/window.

Homepage: https://github.com/Gregory-K/gajim-omemo-mod

**Warning.** The modifications made to the "OMEMO" plugin are not in any way endorsed by the Gajim Development team. On the contrary, they are considered a **security flaw**. Use "OMEMO Mod" only after careful consideration (see [Reasoning](#Reasoning)). If you aren't absolutely certain you need it, please, prefer the [official one](https://dev.gajim.org/gajim/gajim-plugins/wikis/OmemoGajimPlugin)<sup>(ext)</sup>.

*ref:* [Gajim](https://gajim.org)<sup>(ext)</sup> official "OMEMO" plugin [wiki](https://dev.gajim.org/gajim/gajim-plugins/wikis/OmemoGajimPlugin)<sup>(ext)</sup> and [repository](https://dev.gajim.org/gajim/gajim-plugins)<sup>(ext)</sup>

>Quote: OMEMO Wikipedia [entry](https://en.wikipedia.org/wiki/OMEMO)<sup>(ext)</sup>  
>
>OMEMO is an extension to the Extensible Messaging and Presence Protocol ([XMPP](https://en.wikipedia.org/wiki/XMPP "XMPP")<sup>(ext)</sup>) for multi-client [end-to-end encryption](https://en.wikipedia.org/wiki/End-to-end_encryption "End-to-end encryption")<sup>(ext)</sup> developed by Andreas Straub. According to Straub, OMEMO uses the [Double Ratchet Algorithm](https://en.wikipedia.org/wiki/Double_Ratchet_Algorithm "Double Ratchet Algorithm")<sup>(ext)</sup> (Axolotl Ratchet protocol) "to provide multi-end to multi-end encryption, allowing messages to be synchronized securely across multiple clients, even if some of them are offline".  


## Current DEV State

For the time being, the "OMEMO Mod" works as intended, but it's still just a **draft hack** that covers personal needs. It does nothing more or less than its description and it doesn't "touch" any other part of the "OMEMO" source code.

The current `expose_all` branch flirts with the idea of exposing all the hardcoded constants as user configurable values, although I cannot see a practical reason behind that yet. Warning messages have been placed in the REAME.md file and the "OMEMO configuration" panel/window.

The `gajim_1.3` branch of the [gajim-plugins](https://dev.gajim.org/gajim/gajim-plugins)<sup>(ext)</sup> repository is being used as source code, and the following versions of Gajim are **supported**:  
. min Gajim version: 1.2.91  
. max Gajim version: 1.3.90


## Installation

Information on how to [install](#Procedure) or [update](#Updating-Procedure) this plugin.

### Auxiliary Information

This altered plugin shares the same manifest `short_name` with the original for the sole purpose of aiding the user in ensuring that only one OMEMO plugin will be loaded.

Its version will always be one or more decimal places larger than the official one, to secure that it will be loaded instead of the Gajim's "installed by default" one.

**Attention.** Keep in mind that the Gajim "Plugin Installer" cannot auto-update the "OMEMO Mod". In case of a newer official version, since both plugins share the same manifest `short_name`, it will revert-update to the official one. "OMEMO Mod" can only be updated manually, as per the [directions](#Updating-Procedure) bellow.

"OMEMO Mod" saves its extra settings in a [pickle](https://docs.python.org/3/library/pickle.html)<sup>(ext)</sup> file named `omemo_mod.pickle` located in the `pluginsconfig` directory. The "OMEMO" SQLite DB could used, but for now, it's decided to keep the least possible modifications to the "OMEMO" source code.

#### Common Paths

`pluginsconfig` **Path**

| OS          | `pluginsconfig` Path                                      |
| ---         | ---                                                       |
| **Linux**   | `~/.config/gajim/pluginsconfig`                           |
| **Windows** | `C:\Users\<USERNAME>\AppData\Roaming\Gajim\Pluginsconfig` |
| *Any OS*    | `<custom profile path>/pluginsconfig` <sup>[1]</sup>      |

`omemo` **Path**

| OS          | `omemo` Path                                              |
| ---         | ---                                                       |
| **Linux**   | `~/.local/share/gajim/plugins/omemo`                      |
| **Windows** | `C:\Users\<USERNAME>\AppData\Roaming\Gajim\Plugins\omemo` |
| *Any OS*    | `<custom profile path>/plugins/omemo` <sup>[1]</sup>      |

<sub>[1] you custom profile path, if you 're using `Gajim -c <custom profile path>`</sub>

### Procedure

- Backup the previous "OMEMO" plugin. *(optional)*  
  e.g. Create a compressed copy of the `omemo` folder (tar / zip / 7z / etc.).
- Delete all files under the `omemo` path.

AND

- **Easy** : Download the latest [Release](https://github.com/Gregory-K/gajim-omemo-mod/releases) `.tar.gz`/`.7z` file and extract it into the `omemo` path.

OR

- **Advanced** : Clone [this repository](https://github.com/Gregory-K/gajim-omemo-mod) directly into (or clone elsewhere and copy to) the `omemo` path.

### Updating Procedure

- Backup the previous "OMEMO Mod" plugin. *(optional)*  
  e.g. Create a compressed copy of the `omemo` folder (tar / zip / 7z / etc.).
- Delete all files under the `omemo` path.
- In case the "Advanced" settings storage mechanism changes (Release description will contain a warning):
  - Delete `omemo_mod.pickle` located in the `pluginsconfig` path and
  - re-apply your customized settings.

AND

- **Easy** : Download the latest [Release](https://github.com/Gregory-K/gajim-omemo-mod/releases) `.tar.gz`/`.7z` file and extract it into the `omemo` path.

OR

- **Advanced** : Checkout [this repository](https://github.com/Gregory-K/gajim-omemo-mod) directly into (or checkout to your previously chosen location and copy to) the `omemo` path.


## Configuration

Tips on tinkering with the "Advanced" settings of "OMEMO Mod".

**UNACKNOWLEDGED_COUNT**  
*number of unacknowledged messages before a device gets marked as inactive*  
Default: 300  
Allowed: 1 - 9999  
Guide Note: As per usage patterns and SecOps demands.

**DEFAULT_PREKEY_AMOUNT**  
*number of PreKeys to provide in the bundle*  
Default: 100  
Allowed: 80 - 999  
Guide Note: The bundle SHOULD always contain around 100 PreKeys.

**MIN_PREKEY_AMOUNT**  
*minimum number of PreKeys to provide in the bundle*  
Default: 80  
Allowed: 25 - 999  
Guide Note: The bundle MUST always contain at least 25 PreKeys.

**SPK_ARCHIVE_TIME**  
*time period in seconds to keep Singed PreKeys*  
Default: 1296000 seconds = 15 days  
Allowed: 86400 - 5259600 seconds (1 day to 2 months)  
Guide Note: All existing Signed PreKeys that are older than SPK_ARCHIVE_TIME will be deleted.

**SPK_CYCLE_TIME**  
*signed PreKey rotation period*  
Default: 86400 seconds = 24 hours  
Allowed: 86400 - 2629800 seconds (1 day to 1 month)  
Guide Note: Signed PreKeys SHOULD be rotated periodically once a week to once a month. A faster or slower rotation period should not be required.


## Reasoning

Justification for providing the end user with the ability to change the "OMEMO" `UNACKNOWLEDGED_COUNT` ("unacknowledged message count") value.

The ability to change the "unacknowledged message count" value is the main objective of the "OMEMO Mod". The ability to alter the rest of the "Advanced" settings is just for tinkering around and other niche cases.

### Preface

Related reading:  
- [Pitfalls for OMEMO Implementations – Part 1: Inactive Devices](https://blog.jabberhead.tk/2019/12/13/pitfalls-for-omemo-implementations-part-1-inactive-devices/)<sup>(ext)</sup>
- [XEP-0384: Add message counter logic to determine stale devices #709](https://github.com/xsf/xeps/pull/709)<sup>(ext)</sup>

The original "OMEMO" plugin uses constants to define the following:

```python
DEFAULT_PREKEY_AMOUNT = 100
MIN_PREKEY_AMOUNT = 80
SPK_ARCHIVE_TIME = 86400 * 15  # 15 Days
SPK_CYCLE_TIME = 86400         # 24 Hours
UNACKNOWLEDGED_COUNT = 300
```
*ref:* [XEP-0384 Key Exchange](https://xmpp.org/extensions/xep-0384.html#protocol-key_exchange)<sup>(ext)</sup> - [XEP-0384 Bundles](https://xmpp.org/extensions/xep-0384.html#bundles)<sup>(ext)</sup>

> Quote from the "OMEMO" plugin [CHANGELOG](https://dev.gajim.org/gajim/gajim-plugins/-/blob/master/omemo/CHANGELOG)<sup>(ext)</sup>:
>
> ```
> 2.6.45 / 2019-02-21
> - Set device inactive after 300 unacknowledged messages
> ```

#### In summary

`UNACKNOWLEDGED_COUNT`, or plainly "unacknowledged message count", is the maximum number of messages, a threshold, after which a non-receiving device (device ID) will be marked as "inactive" and will no-further receive messages signed with its key.  

The rest of the constants meaning:  
- `DEFAULT_PREKEY_AMOUNT` is the number of PreKeys to provide in the bundle. The bundle SHOULD always contain around 100 PreKeys.
- `MIN_PREKEY_AMOUNT` it the minimum number of PreKeys to provide in the bundle. The bundle MUST always contain at least 25 PreKeys.
- `SPK_ARCHIVE_TIME` is a time period after which all existing SignedPreKeys will be deleted.
- `SPK_CYCLE_TIME` is the Signed PreKey rotation period. Signed PreKeys SHOULD be rotated periodically once a week to once a month. A faster or slower rotation period should not be required.

### Case Study - the Issue

Let's say you are using Gajim (same account) on more than one device.

Device_1 and Device_2 are not always turned-on or "online".

Initially everything works OK. OMEMO encrypted messages are signed for both devices and chat history between the two (or more) devices is being synced successfully.

An **issue** emerges when, for example, Device_1 gets turned-off or disconnected from the Internet (offline) and this state is preserved for a "long" time. *Defining "long" depends on user usage patterns. It can be hours, a day, a week or more.*

If you continue chatting on Device_2 and exchange more than 300 messages, non-receiving Device_1 will be marked as "inactive".

When Device_1 gets turned-on/connected again, Gajim will sync-down the first 300 signed OMEMO encrypted messages and after that, it will fill your chat-log with sequential warnings:  
`00:00:00 Nickname: This message was encrypted with OMEMO, but not for your device.`

While this behaviour is not a bug or an unexpected result, the real **issue** is what can someone do if one wants or needs to invalidate non-receiving devices after 600 messages or after just 1.

### Notes - on the Issue

["Conversations"](https://conversations.im/)<sup>(ext)</sup> app, for example, had a similar issue, [Allow user to configure how long to wait before making OMEMO user inactive #3499](https://github.com/iNPUTmice/Conversations/issues/3499)<sup>(ext)</sup> & [Extend the OMEMO auto expiry to 3 months](https://github.com/iNPUTmice/Conversations/pull/3584)<sup>(ext)</sup>.

"Conversations" is using a maximum time-period value before the invalidation of a device. A hard coded limit of 14 days was chosen, which it has now been extended to 3 months. The end user still has no access to change this, but a 3-month period is a reasonable amount of time.

A time-period based invalidation method of devices is maybe better than counting messages in "flexible security" situations (mainly for mobile devices).

A message count based invalidation method (Gajim) is probably "more secure", although inflexible, if your "inactive" device is stolen or lost. You certainly want the least amount of encrypted messages to be leaked.

### A Solution

*just an opinion*

Both applications, "Conversations" and Gajim in this particular case, chose not to let their aforementioned invalidation methods be user customizable and there definitely were good reasons to do so, considering modern mainstream usage patterns (?). Nevertheless, this "protective" choice is not practicable for everyone and every use-case.

Personally, while being neither a software engineer/developer nor a cryptographer, I think that the "unacknowledged message count" value should be left at the end user's discretion to alter it, according to their usage patterns and/or SecOps demands. The "OMEMO Mod" plugin provides this ability.

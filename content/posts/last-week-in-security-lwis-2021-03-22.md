Title: Last Week in Security (LWiS) - 2021-03-22
Date: 2021-03-22 22:30
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-03-22
Author: Erik
Summary: The latest/greatest mem dumper BOF (<a href="https://twitter.com/anthemtotheego" target="_blank">@anthemtotheego</a>), CLR usage logging evasion (<a href="https://twitter.com/bohops" target="_blank">@bohops</a>), Windows deception engineering (<a href="https://twitter.com/ollieatnccgroup" target="_blank">@ollieatnccgroup</a>), MobileIron enumeration (<a href="https://twitter.com/OptivSourceZero" target="_blank">@OptivSourceZero</a>), common vulns and mis-configs (<a href="https://twitter.com/ShitSecure" target="_blank">@ShitSecure</a>), macOS persistence (<a href="https://twitter.com/theevilbit" target="_blank">@theevilbit</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-03-15 to 2021-03-22.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://research.nccgroup.com/2021/03/16/lending-a-hand-to-the-community-covenant-v0-7-updates/" target="_blank">Lending a hand to the community – Covenant v0.7 Updates</a>. It's great to see a community project like Covenant get contributions from the companies using it on assessments.</li>
<li><a href="https://github.blog/2021-03-18-how-we-found-and-fixed-a-rare-race-condition-in-our-session-handling/" target="_blank">How we found and fixed a rare race condition in our session handling</a>. You probably had to log back into GitHub last week, and this explains why. A rare race condition could have returned data from another user's session.</li>
<li><a href="https://status.azure.com/en-us/status/history/" target="_blank">Azure Key Vault - Intermittent failures - Mitigated (Tracking ID 5LJ1-3CZ)</a>. The 14 hour O365 outage last Monday was caused by key rotation during "complex cross-cloud migration."</li>
<li><a href="https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html" target="_blank">RCE in Google Cloud Deployment Manager</a>. This bug netted a total of $164,674 for the researcher - the highest single-bug award I can recall. Well done!</li>
<li><a href="https://googleprojectzero.blogspot.com/2021/03/in-wild-series-october-2020-0-day.html" target="_blank">In-the-Wild Series: October 2020 0-day discovery</a>. Google Project Zero discovered seven (!) 0days being actively used in the wild as part of a watering hole campaign against Android, Windows, and iOS devices.</li>
<li><a href="https://labs.sentinelone.com/new-macos-malware-xcodespy-targets-xcode-developers-with-eggshell-backdoor/" target="_blank">New macOS malware XcodeSpy Targets Xcode Developers with EggShell Backdoor</a>. With echos of XcodeGhost from 2015, a malicious Xcode project included a script in the build processes to install a backdoor on the developer's machine. This feels very similar to the <a href="https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/" target="_blank">campaign targeting security researchers</a> from January 2021.</li>
<li><a href="https://www.wired.com/story/facebook-red-team-x-vulnerabilities/" target="_blank">Facebook's ‘Red Team X’ Hunts Bugs Beyond the Social Network's Walls</a>. Now this is a good red team scope! Any tech the company relies on can be tested by 'Red Team X.'</li>
<li><a href="https://www.dw.com/en/signal-secure-messaging-app-stops-working-in-china/a-56885528" target="_blank">Signal secure messaging app stops working in China</a>. Surprised it took this long.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://0xpat.github.io/Malware_development_part_8/" target="_blank">Malware development part 8</a>. COFF/BOF loaders are all the rage right now. This post walks through another implementation of a stand-alone COFF (and thus BOF) loader. If you haven't put a BOF loader in your in house remote access tool, you are missing out on lots of community developed capabilities. The resulting <a href="https://github.com/0xpat/COFFInjector" target="_blank">COFFInjector</a> code is available and can be used as a reference.</li>
<li><a href="https://research.nccgroup.com/2021/03/16/deception-engineering-exploring-the-use-of-windows-installer-packages-against-first-stage-payloads/" target="_blank">Deception Engineering: exploring the use of Windows Installer Packages against first stage payloads</a>. Ransomware and other "loud" malware likes to try to uninstall any AV/EDR product as one of the first steps after execution. <a href="https://github.com/nccgroup/UninstalledAppCanary" target="_blank">UninstalledAppCanary</a> detects this by installing a product called "Security" (sure to hit some wildcards) and alerts you to a possible incident if it is uninstalled.</li>
<li><a href="https://www.optiv.com/explore-optiv-insights/source-zero/mobileiron-mdm-contains-static-key-allowing-account-enumeration" target="_blank">MobileIron MDM Contains Static Key Allowing Account Enumeration</a>. Encryption and key management is hard, which is why some vendors will hardcode a key as a way to have encryption without the headache of key management. As soon as this key is discovered however, anything it protects is no longer safe. <a href="https://github.com/optiv/rustyIron" target="_blank">rustyIron</a> is a tool that can leverage this for discovery and more. Hey, at least it wasn't <a href="https://www.youtube.com/watch?v=hGTLIIOb14A" target="_blank">RCE</a> this time?</li>
<li><a href="https://s3cur3th1ssh1t.github.io/The-most-common-on-premise-vulnerabilities-and-misconfigurations/" target="_blank">The most common on premises vulnerabilities &amp; misconfigurations</a>. I love these kinds of posts. So much knowledge packed into a few thousand words. Don't skip this one, there is sure to be at least one new thing in it for you.</li>
<li><a href="https://theevilbit.github.io/beyond/beyond_0005/" target="_blank">Beyond the good ol' LaunchAgents</a>. This full series on macOS persistence is great stuff.</li>
<li><a href="https://bohops.com/2021/03/16/investigating-net-clr-usage-log-tampering-techniques-for-edr-evasion/" target="_blank">Investigating .NET CLR Usage Log Tampering Techniques For EDR Evasion</a>. Running C# or other CLR-based tools leaves usage logs which can be used by AV/EDR or blue teams to detect red team actions. This post goes over what is in these logs, and a few potential ways to stop them from ever being written in the first place.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/xforcered/CredBandit" target="_blank">CredBandit</a>. This BOF is the culmination of many great projects, and allows you to dump process memory using direct syscalls and a custom MiniDumpWriteDump adapted from ReactOS, all without having the dump touch disk, transferring it back via a BeaconPrintf hack. Hopefully this kind of workaround won't be required in the next version of Cobalt Strike. It would be great to have a way to send arbitrary data back to a teamserver in a BOF.</li>
<li><a href="https://github.com/kaluche/bloodhound-quickwin" target="_blank">bloodhound-quickwin</a> is a simple script to extract useful informations from the combo BloodHound + Neo4j. It can help to choose a target for follow on actions.</li>
<li><a href="https://github.com/Malfrats/xeuledoc" target="_blank">xeuledoc</a> can fetch information about any public Google document (doc, sheet, slide, map, drawing, etc).</li>
<li><a href="https://github.com/ZephrFish/Lepus3" target="_blank">Lepus3</a> is a subdomain finder with various API integrations. Learn more in the post: <a href="https://blog.zsec.uk/lepus-fork/" target="_blank">Reviving and Refactoring DNS Enum</a>.</li>
<li><a href="https://github.com/rapid7/metasploit-framework/pull/14907" target="_blank">Add exploit for CVE-2021-1732</a>. The Windows 10 local privilege escalation vulnerability discovered in the wild is now in metasploit - but nothing is stopping you from modifying this code for use in your own framework/tool.</li>
<li><a href="https://github.com/C-Sto/dnsfwd" target="_blank">dnsfwd</a> is a DNS forwarder that only forwards queries for the domains you specify to an upstream host. This is useful for things like DNS beacons where you only want to send beacon related traffic to Cobalt Strike.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/pemistahl/grex" target="_blank">grex</a> is a command-line tool and library for generating regular expressions from user-provided test cases. All you do is give it examples of strings to match and it will generate a regular expression that matches all of them. A great tool for getting a good start on a tough regex.</li>
<li><a href="https://github.com/knavesec/CredMaster" target="_blank">CredMaster</a> is a refactored &amp; improved CredKing password spraying tool that uses FireProx APIs (AWS) to rotate IP addresses, stay anonymous, and beat throttling. More details <a href="https://whynotsecurity.com/blog/credmaster/" target="_blank">here</a>.</li>
<li><a href="https://github.com/hackerscrolls/SecurityTips" target="_blank">SecurityTips</a> is a collection of "HackerScrolls" tips, cheatsheets, and mindmaps.</li>
<li><a href="https://github.com/GoogleCloudPlatform/terraformer" target="_blank">terraformer</a> is a CLI tool to generate terraform files from existing infrastructure (reverse Terraform). Infrastructure to Code</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>

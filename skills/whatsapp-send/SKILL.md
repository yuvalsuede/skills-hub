---
name: whatsapp-send
version: 1.0.0
description: Send messages to WhatsApp contacts and groups
author: cyclop-team
category: communication
tags: [whatsapp, messaging, chat]
verified: true
---

# WhatsApp Send

Sends messages to WhatsApp contacts and groups via WhatsApp Desktop.

## Triggers
- "whatsapp [contact]"
- "send message to [contact] on whatsapp"
- "message [group name] on whatsapp"
- "text [contact] on whatsapp"

## Example Commands
- "Whatsapp John that I'll be late"
- "Send 'Good morning' to the Family group on WhatsApp"
- "Message my boss on WhatsApp: running 10 minutes late"

## How It Works
1. Activates WhatsApp Desktop
2. Searches for the exact contact or group name in the search bar
3. Opens the matching chat
4. Types and sends the message

## Notes
- Always searches for the contact/group by name — never assumes the current chat is correct
- Non-Latin text (Hebrew, Arabic, CJK, etc.) is pasted as a single chunk to avoid spaces between characters
- Group names must match exactly as they appear in WhatsApp

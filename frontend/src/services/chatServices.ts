import type { ChatMessage } from "../types/chatMessage";

export function createUserMessage(content: string): ChatMessage {
    return {
        message_id: crypto.randomUUID(),
        writer: "user",
        content,
        creation_date: new Date().toISOString(),
    };
}

export function createBuddyMessage(content: string): ChatMessage {
    return {
        message_id: crypto.randomUUID(),
        writer: "buddy",
        content,
        creation_date: new Date().toISOString(),
    };
}

export function createWelcomeMessage(): ChatMessage {
    return createBuddyMessage(
        "Hallo! Was möchtest du heute sprechen?"
    );
}

export async function fetchAIAnswer(content: string) {
    const url = 'http://localhost:8000/message/send-message'

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                prompt: content,
            }),
        });
        if (!response.ok){
            throw new Error(`Response status: ${response.status}`);
        }

        const result = (await response.json()).answer
        console.log(result)
        return result
        
    } catch (error) {
        console.error( error instanceof Error ? error.message : '');
    }
}
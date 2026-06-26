export type ChatMessage = {
    message_id: string;
    writer: "user" | "buddy";
    content: string;
    creation_date: string;
};
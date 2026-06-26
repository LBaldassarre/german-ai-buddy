import "./Chat.css";
import Footer from "../components/Footer/Footer";
import Message from "../components/Message/Message";
import { useState, useRef, useEffect } from "react";
import type {ChatMessage } from "../types/chatMessage";
import { createUserMessage, createBuddyMessage, createWelcomeMessage, fetchAIAnswer } from "../services/chatServices"

function Chat() {
    const [chatFormText, setChatFormText] = useState('');
    const textareaRef = useRef<HTMLTextAreaElement>(null);
    const [messages, setMessages] = useState<ChatMessage[]>([createWelcomeMessage()]);

    useEffect(() => {
        const textarea = textareaRef.current;
        if (!textarea) return;

        textarea.style.height = "0px";
        textarea.style.height = `${textarea.scrollHeight}px`;
    }, [chatFormText]);

    async function sendMessage() {
        if (!chatFormText.trim()) return;

        const newUserMessage = createUserMessage(chatFormText)
        const buddyResponse = await fetchAIAnswer(chatFormText)
        const buddyMessage = createBuddyMessage(buddyResponse)

        setMessages(prev => [...prev, newUserMessage, buddyMessage])

        setChatFormText("");
    }

    function handleSubmit(e: React.SubmitEvent<HTMLFormElement>) {
        e.preventDefault();
        sendMessage();
    }

    function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    }

    return (
    <>
        <div className="main-pane">
            <div className="chat-container">
                <div className="cc-chat">
                    {messages.map(message => (
                        <Message
                            key={message.message_id}
                            writer={message.writer}
                            content={message.content}
                        />
                    ))}
                </div>

                <form className="cc-io" onSubmit={handleSubmit}>
                    <div className="cc-io-box">
                        <textarea
                            className="cc-io-type"
                            id="chatFormText"
                            placeholder="Write your message here..."
                            value={chatFormText}
                            ref={textareaRef}
                            onChange={(e) => setChatFormText(e.target.value)}
                            onKeyDown={handleKeyDown}
                        />
                    </div>
                    <button className="cc-io-send" type="submit">
                        <span className="material-symbols-outlined">arrow_upward</span>
                    </button>
                    <button className="cc-io-record" type="submit">
                        <span className="material-symbols-outlined">mic</span>
                    </button>
                </form>

                <Footer/>
            </div>
        </div>
    </>
    )
}

export default Chat

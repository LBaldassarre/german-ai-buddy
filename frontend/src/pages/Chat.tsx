import "./Chat.css";
import Footer from "../components/Footer/Footer";
import { useState, useRef, useEffect } from "react";

function Chat() {
    const [chatFormText, setChatFormText] = useState('');
    const textareaRef = useRef<HTMLTextAreaElement>(null);

    useEffect(() => {
        const textarea = textareaRef.current;
        if (!textarea) return;

        textarea.style.height = "0px";
        textarea.style.height = `${textarea.scrollHeight}px`;
    }, [chatFormText]);

    function sendMessage() {
        if (!chatFormText.trim()) return;

        console.log(chatFormText);

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
                    <div className="cc-message buddy">
                        <div className="cc-message-buddy-content">Hallo! Wie ghet es dir?</div>
                        <div className="cc-message-buddy-translation">Hi! How are you?</div>
                    </div>
                    <div className="cc-message user">
                        <div className="cc-message-user-content">Ich bin gut und dir?</div>
                    </div>
                    <div className="cc-message buddy">
                        <div className="cc-message-buddy-content">Ich bien auch gut, Danke!</div>
                        <div className="cc-message-buddy-translation">I am fine too, thanks!</div>
                    </div>
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

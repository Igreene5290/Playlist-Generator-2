import type React from "react";
import "./MainContainer.css";

export default function MainContainer({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <div className="page">
            <div className="contentBox">{children}</div>
        </div>
    );
}

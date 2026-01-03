import type React from "react";
import "./SideContainer.css";

export default function SideContainer({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <div className="panels">
            <div className="sideBox">{children}</div>
        </div>
    );
}
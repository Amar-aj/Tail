// File Upload Drag and Drop Support
export function setupFileUploadDragDrop(elementId, inputElementId, dotNetRef) {
  const element = document.getElementById(elementId);
  const inputElement = document.getElementById(inputElementId);

  if (!element || !inputElement) return;

  // Prevent default drag behaviors
  ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
    element.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
  });

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  // Highlight drop area when item is dragged over it
  element.addEventListener(
    "dragenter",
    (e) => {
      preventDefaults(e);
      element.classList.add("drag-over");
      dotNetRef.invokeMethodAsync("SetDragging", true);
    },
    false
  );

  element.addEventListener(
    "dragover",
    (e) => {
      preventDefaults(e);
      element.classList.add("drag-over");
      dotNetRef.invokeMethodAsync("SetDragging", true);
    },
    false
  );

  element.addEventListener(
    "dragleave",
    (e) => {
      preventDefaults(e);
      // Only remove if we're actually leaving the element
      if (!element.contains(e.relatedTarget)) {
        element.classList.remove("drag-over");
        dotNetRef.invokeMethodAsync("SetDragging", false);
      }
    },
    false
  );

  // Handle dropped files
  element.addEventListener(
    "drop",
    (e) => {
      preventDefaults(e);
      element.classList.remove("drag-over");
      dotNetRef.invokeMethodAsync("SetDragging", false);

      const dt = e.dataTransfer;
      const files = dt.files;

      if (files && files.length > 0) {
        try {
          // Create a new FileList-like object and assign to input
          const dataTransfer = new DataTransfer();
          for (let i = 0; i < files.length; i++) {
            const file = files[i];
            // Ensure file is properly added and has valid size
            if (file && file.size > 0) {
              dataTransfer.items.add(file);
            }
          }

          // Only proceed if we have valid files
          if (dataTransfer.files.length > 0) {
            // Clear existing files first
            inputElement.value = "";

            // Set the new files
            inputElement.files = dataTransfer.files;

            // Use a small timeout to ensure files are set, then trigger change
            setTimeout(() => {
              // Verify files are set
              if (inputElement.files && inputElement.files.length > 0) {
                // Create and dispatch change event
                const changeEvent = new Event("change", {
                  bubbles: true,
                  cancelable: true,
                });
                inputElement.dispatchEvent(changeEvent);
              } else {
                console.warn("Files were not properly set on input element");
              }
            }, 10);
          } else {
            console.warn("No valid files to add");
          }
        } catch (error) {
          console.error("Error handling file drop:", error);
        }
      }
    },
    false
  );

  return {
    dispose: () => {
      ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
        element.removeEventListener(eventName, preventDefaults, false);
        document.body.removeEventListener(eventName, preventDefaults, false);
      });
    },
  };
}

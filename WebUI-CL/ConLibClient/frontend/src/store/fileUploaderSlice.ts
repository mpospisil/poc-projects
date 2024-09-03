import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export  interface FileUploaderState {
  isLoading: boolean;
  error: string | null;
}

const initialState: FileUploaderState = {
  isLoading: false,
  error: null,
};

const fileUploaderSlice = createSlice({
  name: 'fileUploader',
  initialState,
  reducers: {
    uploadFileRequest: (state) => {
      state.isLoading = true;
      state.error = null;
    },
    uploadFileSuccess: (state) => {
      state.isLoading = false;
    },
    uploadFileFailure: (state, action: PayloadAction<string>) => {
      state.isLoading = false;
      state.error = action.payload;
    },
  },
});

export const {
  uploadFileRequest,
  uploadFileSuccess,
  uploadFileFailure,
} = fileUploaderSlice.actions;

export default fileUploaderSlice.reducer;
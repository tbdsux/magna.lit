<template>
  <main class="flex flex-col lg:flex-row items-start justify-between">
    <Sidebar />

    <div class="w-full lg:w-4/5 xl:w-5/6 ml-auto">
      <slot />
    </div>
  </main>
</template>
